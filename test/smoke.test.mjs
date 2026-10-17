import test from 'node:test'
import assert from 'node:assert/strict'
import { apply, loadDefinition, parseFrontmatter } from '../plugin/index.js'

test('SKILL.md 解析成合法的注册定义', () => {
  const def = loadDefinition()
  assert.equal(def.name, 'ctf-solve-teach')
  assert.match(def.name, /^[a-z0-9]+(-[a-z0-9]+)*$/)
  assert.ok(def.description.length > 20)
  assert.ok(def.content.length > 1000, '正文应该是完整 SKILL.md 内容')
  assert.equal(def.content.includes('---\nname:'), false, 'frontmatter 必须剥离')
  assert.equal(def.resourceBase.kind, 'directory')
  assert.equal(def.source, 'runtime')
})

test('apply 注册 skill 并在 dispose 时注销', () => {
  const calls = []
  const disposed = []
  const ctx = {
    skills: {
      register: (definition) => {
        calls.push(definition)
        return () => disposed.push(definition.name)
      },
    },
    on: (event, fn) => {
      if (event === 'dispose') ctx._dispose = fn
    },
    logger: { info() {}, warn() {} },
  }
  apply(ctx)
  assert.equal(calls.length, 1)
  assert.equal(calls[0].name, 'ctf-solve-teach')
  ctx._dispose()
  assert.deepEqual(disposed, ['ctf-solve-teach'])
})

test('frontmatter 支持块标量与引号标量', () => {
  const text = '---\nname: a-b\ndescription: |\n  第一行\n  第二行\nmetadata:\n  author: "x"\n---\n正文开始\n'
  const { data, body } = parseFrontmatter(text)
  assert.equal(data.name, 'a-b')
  assert.equal(data.description, '第一行\n第二行')
  assert.equal(body.trim(), '正文开始')
})

test('没有 frontmatter 时正文原样返回', () => {
  const { data, body } = parseFrontmatter('# 标题\n内容')
  assert.deepEqual(data, {})
  assert.equal(body, '# 标题\n内容')
})
