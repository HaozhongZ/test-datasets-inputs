# 生成能力测试输入集

这里发布可直接用于批量测试的输入数据。各类测试集分别放在 `suites/` 下。

## 信息图 v1.0.0

- 文件：[`suites/infographic/v1.0.0/input.json`](suites/infographic/v1.0.0/input.json)
- 数量：120 条，每条数据表不同。
- 格式：JSON 数组；每条包含 `id`、`source_id`、`user_question`、`table.headers` 和 `table.rows`。
- 用法：逐条将问句与表格提交给被测生成能力，按 `id` 保存产物。

## 并购视频 v1.0.0

- 文件：[`suites/merger-video/v1.0.0/input.json`](suites/merger-video/v1.0.0/input.json)
- 数量：8 条。
- 格式：JSON 数组；每条包含 `id`、`title`、`source_file`、`input` 和 `original_markdown`。`input` 内有 `annotated_script`、`references` 和 `plain_script`。
- 用法：按被测能力所需的字段提交案例，并按 `id` 保存产物。公开副本将原文件中 32 处他人电脑的绝对路径替换为“本地路径已移除”，原文件未修改。

此仓库只包含测试输入。信息图的期望图型、insight、评分规则和盲测 ID 映射由维护者独立保存，测试前不提供给被测系统。部分案例使用控制性模拟数据；请不要把测试内容当作最新公司披露或投资事实。

运行 `python3 tools/validate.py` 检查输入结构、ID 和信息图表格唯一性。

目前未给数据内容指定开放许可证；如需再分发或改编，请先联系仓库维护者确认使用范围。
