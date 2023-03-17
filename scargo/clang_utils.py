from pathlib import Path
from typing import Iterable, Tuple

from clang.cindex import Index, TokenKind


def get_comment_lines(file_path: Path) -> Iterable[Tuple[int, str]]:
    index = Index.create()
    translation_unit = index.parse(str(file_path), args=["-x", "c++"])

    for token in translation_unit.cursor.get_tokens():
        if token.kind == TokenKind.COMMENT:
            yield from enumerate(
                # there's a bug in types-clang: https://github.com/tgockel/types-clang/issues/8
                # when it's fixed in a new release, we can remove the type ignore comment
                token.spelling.splitlines(keepends=False),
                start=token.extent.start.line,  # type: ignore[attr-defined]
            )
