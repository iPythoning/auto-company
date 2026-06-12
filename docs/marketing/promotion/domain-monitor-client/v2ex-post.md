# V2EX 推广内容

## 发布节点：分享创造

**标题：** 做了一个零后端的域名/SSL 过期监控工具——单个 HTML 文件，永久免费

**正文：**

作为一个独立开发者，域名过期忘记续费、SSL 证书过期导致网站挂掉这种事，应该每个人都经历过吧。

周末写了个小工具解决这个问题：[Domain Monitor Client](https://ipythoning.github.io/domain-monitor-client/)

## 特点

- **零后端**：就一个 17KB 的 HTML 文件，托管在 GitHub Pages
- **零成本**：没有服务器，没有数据库，永久免费
- **零注册**：不需要账号，打开即用
- **数据本地存储**：域名列表存在浏览器的 localStorage，不上传任何数据

## 技术原理

传统 WHOIS 走的是 TCP 43 端口，浏览器没法直接调。但这个工具用的是 **RDAP**（Registration Data Access Protocol），一个基于 HTTPS 的 RESTful JSON API，浏览器可以直接请求。

不同后缀的域名走不同的 RDAP 服务器：
- .com/.net → Verisign 的 RDAP
- .org → PIR 的 RDAP  
- .io → Nic.io 的 RDAP
- 等等

SSL 证书信息通过 [crt.sh](https://crt.sh) 查询，这是 Google 运营的证书透明度日志，支持 CORS，无需 API Key。

## 适用场景

- 手里管着好几个域名的独立开发者
- 给客户做网站的 freelancer
- 想自建监控但又不想维护后端的人
- 临时需要查一批域名的过期时间

## 自部署

下载 index.html 丢到任何静态服务器就行，Nginx/Apache/GitHub Pages/甚至本地 file:// 打开都能用。

线上 Demo：https://ipythoning.github.io/domain-monitor-client/
GitHub：https://github.com/iPythoning/domain-monitor-client

欢迎试用，欢迎提 issue。特别是如果你用的域名后缀 RDAP 查不到的话，告诉我我来修。

---

## 备选标题（测试点击率）

- 「再也不怕域名过期了——一个零成本的域名监控方案」 
- 「单文件 HTML 实现的域名+SSL 到期监控，永久免费」
- 「分享一个零后端零成本的域名监控小工具」
