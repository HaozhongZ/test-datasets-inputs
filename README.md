# 生成能力测试输入集

按测试对象保存批量输入。选择对应的 `input.json`，逐条提交案例并按 `id` 记录结果。

| 测试集 | 测试对象与内容 | 输入 |
| --- | --- | --- |
| [信息图](suites/infographic/v1.0.0/input.json) | 信息图生成；120 条中文问句及各不相同的数据表，覆盖时间、比较、构成、排名等数据关系。 | `user_question` + `table` |
| [AIME 信息图英文表格](suites/aime-infographic-english/v1.0.0/input.json) | AIME 上线的信息图生成；120 条英文问句及英文表格，测试数据呈现与图表选择。部分案例使用模拟数据。 | `user_question` + `table` |
| [AIME 信息图纯问句](suites/aime-infographic-questions/v1.0.0/input.json) | AIME 信息图生成；100 条英文金融问句，测试从问句获取数据、判断是否适合成图以及生成信息图。 | 仅提交 `user_question` |
| [并购视频](suites/merger-video/v1.0.0/input.json) | 并购视频生成；8 条分段文案，包含旁白、画面提示与参考资料。 | `input` 中的文案与参考资料 |
| [HTML 图表动画](suites/html-chart-animation/v1.0.0/input.json) | HTML 图表动画生成；90 条叙述与数据表，测试叙述和图表动画的对应关系。 | `input` 中的 `intent`、`narration`、`tables` |
| [K线解读视频动画](suites/kline-video-animation/v1.0.0/input.json) | 短K线解读动画数据；100 条含合成 OHLCV 数据、动画提示和视频范例的输入。 | `input` 中的 `intent`、`narration`、`tables`；`video_reference` 只作视觉范例 |
| [短时 K线解读视频](suites/kline-video-narrative/v1.0.0/input.json) | 短K线解读动画数据；18 条约 45 秒的B站、抖音视频参考输入，覆盖形态、逐K复盘、价格行为与结构确认。行情数据为合成样例。 | `input` 中的 `intent`、`narration`、`tables`、`video_reference` 与 `animation_hints` |

信息图的期望结果与评分材料不在此输入仓库中。运行 `python3 tools/validate.py` 可检查各测试集的结构和 ID。
