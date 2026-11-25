"""Entry for make.fun bounty: The Word You'd Delete From the Dictionary.

The word to delete is "Worcestershire" -- the English town and sauce name
whose spelling has almost nothing to do with its pronunciation
("WUSS-ter-sher"). It is the classic example of a word that breaks every
phonetic rule a learner is taught: three syllables spoken where nine
letters are written, a silent "ce", and a "shire" that collapses to "sher".
Deleting it from the dictionary would spare every non-native speaker the
embarrassment of reading it aloud, and the sauce could keep its name --
nobody spells it out loud anyway.

Writes the single word to /output/entry.txt first, then a byte-identical
copy to entry.txt in the repo root (best effort: the grader sandbox mounts
the repo read-only, so a failed copy must never crash the run).
"""

import os

WORD = "Worcestershire"


def copy_to_repo_root(data: bytes) -> None:
    """Write a byte-identical copy of the entry to entry.txt in the repo root.

    The grader sandbox mounts the repository read-only, so this copy can
    fail with an OSError; that is expected and must never crash the run.
    The authoritative output is /output/entry.txt, written before this.
    """
    try:
        with open("entry.txt", "wb") as f:
            f.write(data)
    except OSError:
        pass


def main() -> None:
    data = WORD.encode("utf-8")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    copy_to_repo_root(data)


if __name__ == "__main__":
    main()
