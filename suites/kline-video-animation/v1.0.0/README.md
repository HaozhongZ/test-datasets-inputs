# K线解读视频动画生成测试集 1.0.0

`input.json`包含100条案例，沿用`html-chart-animation`的`id`与`input.intent`、`input.narration`、`input.tables`输入形式。每条表格包含24根OHLCV合成K线；`animation_hints`给出画面比例、时长、风格标签和动作时间线；`video_reference`提供公开视频和片段时间码供风格参考。

## 数据说明

- OHLCV是确定性合成演示数据，不是来源视频行情的转录，也不应被用于交易或行情结论。
- 视频只作为画风、运镜与标注范例。生成器可仅凭`intent`、`narration`、`tables`和`animation_hints`运行；无需读取参考视频。需要逐帧贴近范例时，才查看`video_reference`。
- 视频素材没有复制进仓库；来源链接和时间码作为引用保留。
- 输入集不包含期望成片或评分标准，适合跨生成器共享与比较。

运行仓库结构校验：

```bash
python3 tools/validate.py
```
