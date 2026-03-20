# ACM Computing Survey Project Structure

## File Organization

### Main Files
- `survey.tex` - 主要LaTeX文档
- `survey.pdf` - 编译后的PDF文档
- `sample-base.bib`, `software.bib` - BibTeX引用文件
- `name.tex` - 作者信息
- `ACM-Reference-Format.bst`, `acmart.cls` - ACM期刊样式文件

### Data Files
- `1.md` - 329篇论文列表
- `Section_4.3_Literature_Mapping.md` - 4.3节文献映射
- `README.txt` - 原始说明文件

### Folders
- `scripts/` - Python脚本文件
  - `arxiv_search.py` - arXiv搜索脚本
  - `search_papers.py` - 论文搜索
  - `update_table.py` - 表格更新
  - `temp_*.py` - 临时脚本
- `latex_build/` - LaTeX编译生成的文件
- `assets/` - 图片和其他资源文件

## How to Use

1. 编辑 `survey.tex` 进行文档修改
2. 使用 `scripts/` 下的Python脚本进行数据处理
3. 编译LaTeX生成新的PDF文档
4. 生成的临时文件会存放在 `latex_build/` 文件夹中

## Notes

- 已添加 `.gitignore` 文件排除临时文件
- 文件夹结构保持源文件和生成文件分离
- 便于版本控制和项目管理