# Gradle OSS Development Memo

## Entry Pointの確認ログ

| No. | content                           | class                   | link                                                                                                                                                                                                             |
|-----|-----------------------------------|-------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Entry Point                       |                         | [Command実行時の呼び出し](https://github.com/kackey0-1/gradle/blob/af509fd7e9ddcb85de364bf5b6d131673615935a/gradlew#L206-L210)                                                                                           |
| 2   | Main Method in GradleWrapperMain  | GradleWrapperMain       | [main method](https://github.com/kackey0-1/gradle/blob/2ec02f4919c1690debaa604f889f0f0a42dce6a1/subprojects/wrapper/src/main/java/org/gradle/wrapper/GradleWrapperMain.java#L38)                                 |
| 3   | Execution                         | WrapperExecutor         | [execution method](https://github.com/kackey0-1/gradle/blob/2ec02f4919c1690debaa604f889f0f0a42dce6a1/subprojects/wrapper-shared/src/main/java/org/gradle/wrapper/WrapperExecutor.java#L108)                      |
| 4   | start method                      | BootstrapMainStarter    | [start method](https://github.com/kackey0-1/gradle/blob/81263540fa33ec75aa381c505cce72a5471fcbcb/subprojects/wrapper-shared/src/main/java/org/gradle/wrapper/BootstrapMainStarter.java#L26)                      |
| 5   | main method through invoke method | GradleMain              | [main method through invoke method](https://github.com/kackey0-1/gradle/blob/c24d29c30c9c3e4e2af47a7eceff75391b9a9059/subprojects/bootstrap/src/main/java/org/gradle/launcher/GradleMain.java#L24)               |
| 6   | run method through invoke method  | ProcessBootstrap        | [run method through invoke method](https://github.com/kackey0-1/gradle/blob/5c01e863d7fd0129ad758da6390e4ea33895f6e3/subprojects/launcher/src/main/java/org/gradle/launcher/bootstrap/ProcessBootstrap.java#L35) |
| 7   | runNoExit method                  | ProcessBootstrap        | [runNoExit method](https://github.com/kackey0-1/gradle/blob/5c01e863d7fd0129ad758da6390e4ea33895f6e3/subprojects/launcher/src/main/java/org/gradle/launcher/bootstrap/ProcessBootstrap.java#L45)                 |
| 8   | Main class's main method          | Main                    | [Main.main method through invoke method](https://github.com/kackey0-1/gradle/blob/7e461f7a72d56c04d94c436ccdb1ef184fa72f5b/subprojects/launcher/src/main/java/org/gradle/launcher/Main.java#L30)                 |
| 9   | Main class's run method           | Main extends EntryPoint | [Main.run extends EntryPoint](https://github.com/kackey0-1/gradle/blob/5c01e863d7fd0129ad758da6390e4ea33895f6e3/subprojects/launcher/src/main/java/org/gradle/launcher/bootstrap/EntryPoint.java#L47)            |
| 10  | Main doAction method              | Main                    | [Main.doAction method](https://github.com/kackey0-1/gradle/blob/7e461f7a72d56c04d94c436ccdb1ef184fa72f5b/subprojects/launcher/src/main/java/org/gradle/launcher/Main.java#L35)                                   |
|||||
|||||
|||||
