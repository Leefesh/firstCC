"""将 Cursor 编辑器显示语言改为中文"""
import json
import os
import shutil
from pathlib import Path

# Cursor 配置文件路径
LOCALE_FILE = Path(os.environ["APPDATA"]) / "Cursor" / "User" / "locale.json"
EXTENSIONS_DIR = Path.home() / ".cursor" / "extensions"
ARGV_FILE = Path.home() / ".cursor" / "argv.json"

def get_installed_language_packs():
    """检查已安装的语言包"""
    packs = []
    if EXTENSIONS_DIR.exists():
        for d in EXTENSIONS_DIR.iterdir():
            if d.is_dir() and "language-pack" in d.name:
                packs.append(d.name)
    return packs

def set_locale(locale="zh-cn"):
    """设置 Cursor 显示语言"""
    LOCALE_FILE.parent.mkdir(parents=True, exist_ok=True)

    current = {}
    if LOCALE_FILE.exists():
        current = json.loads(LOCALE_FILE.read_text(encoding="utf-8"))

    current["locale"] = locale
    LOCALE_FILE.write_text(
        json.dumps(current, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8"
    )
    return current.get("locale")

def main():
    print("=" * 50)
    print("Cursor 显示语言设置工具")
    print("=" * 50)

    # 1. 设置语言为中文
    old_locale = set_locale("zh-cn")
    print(f"\n[OK] locale.json 已更新: {old_locale} -> zh-cn")

    # 2. 检查语言包
    packs = get_installed_language_packs()
    if packs:
        print(f"[OK] 已安装中文语言包: {packs[0]}")
    else:
        print("[!] 未检测到中文语言包，请在 Cursor 扩展商店搜索")
        print("    'Chinese Language Pack' 或 'ms-ceintl.vscode-language-pack-zh-hans' 并安装")

    # 3. 重启提示
    print("\n" + "-" * 50)
    print("请重启 Cursor 使设置生效 (Ctrl+Shift+P → Reload Window)")
    print("-" * 50)

if __name__ == "__main__":
    main()
