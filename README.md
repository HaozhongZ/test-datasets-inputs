# 生成能力测试输入集

这里发布可直接用于批量测试的输入数据。首批为信息图生成测试集；后续可在 `suites/` 下加入 HTML 视频、混剪视频和公司介绍视频等测试集。

## 信息图 v1.0.0

- 文件：[`suites/infographic/v1.0.0/input.json`](suites/infographic/v1.0.0/input.json)
- 数量：120 条，每条数据表不同。
- 格式：JSON 数组；每条包含 `id`、`source_id`、`user_question`、`table.headers` 和 `table.rows`。
- 用法：逐条将问句与表格提交给被测生成能力，按 `id` 保存产物。

此仓库只包含盲测输入。期望图型、insight、评分规则和盲测 ID 映射由维护者独立保存，测试前不提供给被测系统。部分案例使用控制性模拟数据；请不要把测试表当作最新公司披露或投资事实。

运行 `python3 tools/validate.py` 检查输入结构、ID 和表格唯一性。

目前未给数据内容指定开放许可证；如需再分发或改编，请先联系仓库维护者确认使用范围。
