# Gradleについて

## Gradleとは

- 一般的なbuildツール
- タスクベースを中心のモデル
  - Directed Acyclic Graphsのようにタスクを設定することが可能
- Gradleはいくつかのbuild phaseを持っている
  - Initialization
  - Configuration
  - Execution
- より直感的にbuild scriptを理解することが可能

## mavenとの違いは？

- Mavenはビルドの手順を定義するための言語として、XMLを用いる
  - XMLでは、ぱっと見ただけでは、どのような処理をしているかなかなかわかりにくい

## なぜ Kotlin を DSL に使うのか

- 知らないシンタックスやメソッドを推測する手段が少ない
- Kotlin だと IDE 上から型が推測しやすい

## Gradle Handson

```bash
gradle init --type 
```


