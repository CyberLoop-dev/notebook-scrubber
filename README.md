<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:111827,100:#38bdf8&height=180&section=header&text=Notebook%20Scrubber&fontSize=42&fontColor=ffffff" alt="Notebook Scrubber banner"/></p>
<p align="center"><img src="https://readme-typing-svg.demolab.com?font=Fira+Code&weight=600&size=20&pause=1000&color=38BDF8&center=true&vCenter=true&width=650&lines=Clean%20notebooks.%20Keep%20the%20story." alt="Animated project tagline"/></p>
<p align="center">
  <img src="https://img.shields.io/github/license/CyberLoop-dev/notebook-scrubber?style=for-the-badge" alt="License"/>
  <img src="https://img.shields.io/github/languages/top/CyberLoop-dev/notebook-scrubber?style=for-the-badge" alt="Top language"/>
  <img src="https://img.shields.io/github/stars/CyberLoop-dev/notebook-scrubber?style=for-the-badge" alt="Stars"/>
  <img src="https://img.shields.io/github/last-commit/CyberLoop-dev/notebook-scrubber?style=for-the-badge" alt="Last commit"/>
</p>
<p align="center"><img src="./assets/icon.svg" width="150" alt="Notebook Scrubber illustration"/></p>

## 🚀 Overview

Notebook Scrubber is a privacy-friendly CLI that removes bulky cell outputs and execution counters from Jupyter notebooks. It makes reviews cleaner and keeps generated output out of version control without changing cell source.

## ✨ Features

- 🧽 Remove code-cell outputs and execution counts
- 🛟 Create a backup before in-place edits
- 🔎 Check whether a notebook needs cleaning in CI
- 📄 Preserve markdown cells and source content

## 🎬 Demo

~~~bash
python main.py analysis.ipynb --check
~~~

No hosted service or account is required.

## ⚡ Quick Start

~~~bash
git clone https://github.com/CyberLoop-dev/notebook-scrubber.git
cd notebook-scrubber
python main.py --help
~~~

Python 3.10 or newer is recommended.

## 🧰 Tech Stack

- 🐍 Python 3.10+
- 📦 Python standard library only
- 🧪 unittest for tests

## 📁 Folder Structure

~~~text
notebook-scrubber/
├── assets/icon.svg
├── tests/test_main.py
├── .gitignore
├── LICENSE
├── README.md
├── main.py
├── pyproject.toml
└── requirements.txt
~~~

## 🗺️ Roadmap

- [x] 🧩 Working command-line core
- [x] 🧪 Standard-library tests
- [ ] 📊 Optional richer reports
- [ ] 🧰 More edge-case fixtures

## 🤝 Contributing

Issues and pull requests are welcome. Keep changes focused, add tests for new behavior, and use clear commit messages.

## 📄 License

Released under the MIT License. See [LICENSE](LICENSE).

<p align="center"><img src="https://capsule-render.vercel.app/api?type=waving&color=0:#38bdf8,100:111827&height=110&section=footer" alt="Animated wave footer"/></p>
