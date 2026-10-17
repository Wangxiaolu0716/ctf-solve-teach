/**
 * dsh-ctf-solve-teach — DeepSeek Harness 插件
 *
 * 把「教学式 CTF 解题」skill 注册进 ctx.skills：安装即出现在技能目录里，
 * 模型可像本地 skill 一样加载。零依赖，只读包内的 skills/ctf-solve-teach/SKILL.md。
 *
 * 由 cordis.patch.yml 挂载（package.json 的 dsh.bundle.patch）。
 */
import { readFileSync } from 'node:fs'
import { fileURLToPath } from 'node:url'

const SKILL_DIR = fileURLToPath(new URL('../skills/ctf-solve-teach/', import.meta.url))
const SKILL_FILE = SKILL_DIR + 'SKILL.md'

const FALLBACK_DESCRIPTION =
  '教学式 CTF / 安全解题：边解边讲套路、工具与知识点，收尾在 solves/<题目名>/ 生成可复现 Writeup。'

/** Cordis 插件名（仅用于日志与调试）。 */
export const name = 'ctf-solve-teach-skills'
/** 依赖 skills 服务；宿主未挂载时会自动等待，不会崩溃。 */
export const inject = ['skills']

/**
 * 拆出 YAML frontmatter 与正文。
 * 只支持本包实际用到的语法：单行标量、引号标量、块标量（| / >）。
 */
export function parseFrontmatter(text) {
  const match = /^\uFEFF?---[ \t]*\r?\n([\s\S]*?)\r?\n---[ \t]*(?:\r?\n|$)/.exec(text)
  if (!match) return { data: {}, body: text }

  const data = {}
  let key = null
  let buffer = []
  const flush = () => {
    if (key === null) return
    const indents = buffer.filter((line) => line.trim() !== '').map((line) => /^[ \t]*/.exec(line)[0].length)
    const min = indents.length > 0 ? Math.min(...indents) : 0
    const value = buffer.map((line) => line.slice(min)).join('\n').trim()
    if (value) data[key] = value
    key = null
    buffer = []
  }

  for (const raw of match[1].split('\n')) {
    const line = raw.replace(/\r$/, '')
    const kv = /^([A-Za-z0-9_-]+):[ \t]*(.*)$/.exec(line)
    if (kv) {
      flush()
      const value = kv[2].trim()
      if (/^[|>][-+]?$/.test(value) || value === '') {
        key = kv[1]
        buffer = []
      } else {
        data[kv[1]] = value.replace(/^["']|["']$/g, '')
      }
      continue
    }
    if (key !== null) buffer.push(line)
  }
  flush()
  return { data, body: text.slice(match[0].length) }
}

function warn(ctx, message) {
  const text = '[dsh-ctf-solve-teach] ' + message
  if (typeof ctx.logger?.warn === 'function') ctx.logger.warn(text)
  else console.warn(text)
}

/** 读取 SKILL.md 并构造注册定义；失败时返回 null（不阻断宿主启动）。 */
export function loadDefinition() {
  const text = readFileSync(SKILL_FILE, 'utf8')
  const { data, body } = parseFrontmatter(text)
  const content = body.trim()
  if (!content) throw new Error('SKILL.md 正文为空')
  return {
    name: data.name || 'ctf-solve-teach',
    description: data.description || FALLBACK_DESCRIPTION,
    content,
    resourceBase: { kind: 'directory', path: SKILL_DIR },
    source: 'runtime',
  }
}

export function apply(ctx) {
  let definition
  try {
    definition = loadDefinition()
  } catch (error) {
    warn(ctx, '读取 SKILL.md 失败，技能未注册：' + (error?.message ?? String(error)))
    return
  }

  const dispose = ctx.skills.register(definition)
  if (typeof dispose === 'function') ctx.on?.('dispose', dispose)

  if (typeof ctx.logger?.info === 'function') {
    ctx.logger.info('[dsh-ctf-solve-teach] 已注册技能 "' + definition.name + '"')
  }
}
