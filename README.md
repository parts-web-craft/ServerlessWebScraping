## 環境
* Python3.7
* serverless-chrome: [v1.0.0-37](https://github.com/adieuadieu/serverless-chrome/releases/tag/v1.0.0-37)
* ChromeDriver: [v2.37](https://chromedriver.storage.googleapis.com/index.html?path=2.37/)
* [serverless framework](https://serverless.com/)
* AWS Lambda


## 構築&デプロイ
* serverless frameworkをインストール。（AWSキー周りは公式Docを参考）
```shell script
npm install -g serverless
```

* node_modules
```shell script
npm ci
```

* deploy
```shell script
sls deploy
```

※トリガーはAPI Gateway