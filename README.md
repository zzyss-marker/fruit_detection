# fruit_detection


从你的日志中可以看到，你的 `git push` 操作失败了，因为你尝试推送的文件 `data/fruits_360.zip` 超过了 GitHub 的文件大小限制（100MB）。要解决这个问题，你可以使用 Git LFS（Git Large File Storage）来管理大文件。以下是解决方案的步骤：

1. **安装 Git LFS**:
   如果你还没有安装 Git LFS，可以通过以下命令安装：

   ```bash
   git lfs install
   ```
2. **跟踪大文件**:
   使用 Git LFS 跟踪大文件：

   ```bash
   git lfs track "data/fruits_360.zip"
   ```
3. **提交 .gitattributes 文件**:
   上一步会在你的仓库中创建一个 `.gitattributes` 文件，需要将其添加并提交到仓库：

   ```bash
   git add .gitattributes
   git commit -m "Track large file with Git LFS"
   ```
4. **重新添加并提交大文件**:
   需要重新添加和提交你的大文件：

   ```bash
   git add data/fruits_360.zip
   git commit -m "Add large file using Git LFS"
   ```
5. **推送到远程仓库**:
   最后，推送你的更改到远程仓库：

   ```bash
   git push origin main
   ```
