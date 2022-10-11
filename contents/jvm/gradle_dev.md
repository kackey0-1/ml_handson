# Gradle OSS Development Memo

## ローカルでのbuild方法

1. To create a Gradle distribution from the source tree you can run either of the following:
    ```bash
    ./gradlew :distributions-full:binDistributionZip
    ```
    This will create a minimal distribution at `subprojects/distributions-full/build/distributions/gradle-<version>-bin.zip`, just what's needed to run Gradle (i.e. no sources nor docs).

2. You can then use it as a Gradle Wrapper local distribution in a Gradle based project by using a `file:/` URL pointing to the built distribution:
    ```bash
    ./gradlew wrapper --gradle-distribution-url=file:/path/to/gradle-<version>-bin.zip
    ```
3. To create a full distribution (includes sources and docs):
    ```bash
    ./gradlew :distributions-full:allDistributionZip
    ```
4. The full distribution will be created at `subprojects/distributions-full/build/distributions/gradle-<version>-all.zip`. You can then use it as a Gradle Wrapper local distribution:
    ```bash
    ./gradlew wrapper --gradle-distribution-url=file:/path/to/gradle-<version>-all.zip
    ```

## Entry Pointの確認ログ

| No. | content                           | class                                      | link                                                                                                                                                                                                                             |
|-----|-----------------------------------|--------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1   | Entry Point                       |                                            | [Command実行時の呼び出し](https://github.com/kackey0-1/gradle/blob/af509fd7e9ddcb85de364bf5b6d131673615935a/gradlew#L206-L210)                                                                                                           |
| 2   | Main Method in GradleWrapperMain  | GradleWrapperMain                          | [main method](https://github.com/kackey0-1/gradle/blob/2ec02f4919c1690debaa604f889f0f0a42dce6a1/subprojects/wrapper/src/main/java/org/gradle/wrapper/GradleWrapperMain.java#L38)                                                 |
| 3   | Execution                         | WrapperExecutor                            | [execution method](https://github.com/kackey0-1/gradle/blob/2ec02f4919c1690debaa604f889f0f0a42dce6a1/subprojects/wrapper-shared/src/main/java/org/gradle/wrapper/WrapperExecutor.java#L108)                                      |
| 4   | start method                      | BootstrapMainStarter                       | [start method](https://github.com/kackey0-1/gradle/blob/81263540fa33ec75aa381c505cce72a5471fcbcb/subprojects/wrapper-shared/src/main/java/org/gradle/wrapper/BootstrapMainStarter.java#L26)                                      |
| 5   | main method through invoke method | GradleMain                                 | [main method through invoke method](https://github.com/kackey0-1/gradle/blob/c24d29c30c9c3e4e2af47a7eceff75391b9a9059/subprojects/bootstrap/src/main/java/org/gradle/launcher/GradleMain.java#L24)                               |
| 6   | run method through invoke method  | ProcessBootstrap                           | [run method through invoke method](https://github.com/kackey0-1/gradle/blob/5c01e863d7fd0129ad758da6390e4ea33895f6e3/subprojects/launcher/src/main/java/org/gradle/launcher/bootstrap/ProcessBootstrap.java#L35)                 |
| 7   | runNoExit method                  | ProcessBootstrap                           | [runNoExit method](https://github.com/kackey0-1/gradle/blob/5c01e863d7fd0129ad758da6390e4ea33895f6e3/subprojects/launcher/src/main/java/org/gradle/launcher/bootstrap/ProcessBootstrap.java#L45)                                 |
| 8   | Main class's main method          | Main                                       | [Main.main method through invoke method](https://github.com/kackey0-1/gradle/blob/7e461f7a72d56c04d94c436ccdb1ef184fa72f5b/subprojects/launcher/src/main/java/org/gradle/launcher/Main.java#L30)                                 |
| 9   | Main class's run method           | Main extends EntryPoint                    | [Main.run extends EntryPoint](https://github.com/kackey0-1/gradle/blob/5c01e863d7fd0129ad758da6390e4ea33895f6e3/subprojects/launcher/src/main/java/org/gradle/launcher/bootstrap/EntryPoint.java#L47)                            |
| 10  | Main doAction method              | Main                                       | [Main.doAction method](https://github.com/kackey0-1/gradle/blob/7e461f7a72d56c04d94c436ccdb1ef184fa72f5b/subprojects/launcher/src/main/java/org/gradle/launcher/Main.java#L35)                                                   |
| 11  | create execution command          | convert in DefaultCommandLineActionFactory | [DefaultCommandLineActionFactory.convert](https://github.com/kackey0-1/gradle/blob/439a1668b710ef9a4cd7ac5d2617defda850b0ca/subprojects/launcher/src/main/java/org/gradle/launcher/cli/DefaultCommandLineActionFactory.java#L74) |
| 12  | execute method                    | execute method through WithLogging         | [WithLogging.execute](https://github.com/kackey0-1/gradle/blob/439a1668b710ef9a4cd7ac5d2617defda850b0ca/subprojects/launcher/src/main/java/org/gradle/launcher/cli/DefaultCommandLineActionFactory.java#L314)                    |
|||||
