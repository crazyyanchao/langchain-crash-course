# langchain-crash-course
Build an LangChain app in few minutes! | 快速构建 LangChain 应用程序

>&emsp;&emsp;本项目主要演示基于 Langchain 开发的应用程序，包含 Langchain 和 Autonomous Agents 类程序的示例。

>&emsp;&emsp;LangChain 是一个使用LLMs构建应用程序的工具箱，包含Models、Prompts、Indexes、Memory、Chains、Agents、Callbacks等核心模块。

>&emsp;&emsp;Autonomous Agents（自主代理）是由人工智能驱动的程序，当给定目标时，它们能够为自己创建任务，完成任务，创建新任务，重新确定任务列表的优先级，完成新的顶级任务，循环（递归的思想）直到达到目标。
>大概就是你给Autonomous Agents一个任务，比如发一个关于 Autonomous Agents 最新进展的 twitter。他会先去理解分解这个任务目标，然后设定实施计划以及这几个计划的优先级，同时去辩证『冷静』的反思计划有没有漏洞，并将反思应用到执行过程中，然后就是自己不断的去换着关键词搜索总结最近的报道文章，然后是汇总、反思，看看有没有什么遗漏，最后组织成适合推文的语言自动发送。

## 工具
- [短视频脚本创作工具](tool-1)
- [邮件助手](tool-2)

## 测试
- [接口测试](others)

## 相关链接

- [Integrating Neo4j database into langchain ecosystem](https://github.com/tomasonjo/langchain2neo4j)
- [Integrating ONgDB database into langchain ecosystem](https://github.com/ongdb-contrib/langchain2ongdb)
- [NexusGPT](https://nexus.snikpic.io/)

## 项目功能复现
### 配置
- 在根目录下新建`.env`文件，设置对应秘钥信息

### 运行环境
```shell
# 创建虚拟环境
conda env create --name langchain-crash-course --file env.yaml
```

```shell
# 当前环境下的package信息存入名为environment的YAML文件中
conda env export > environment.yaml
```
