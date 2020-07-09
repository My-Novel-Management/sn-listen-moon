#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from config import ASSET
# import scenes
from scenes import Stage


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Story structure
#   4. Plot
#   5. Scenes
#   6. Conte
#   7. Layout
#   8. Draft
#
################################################################

# Constant
TITLE = "月を聴く彼女"
COPY = "月を聴いたことがありますか？"
ONELINE = "約8000字の恋愛短編。目の見えないハープ奏者の彼女の夫は、月が見えるという彼女を理解できずにいた。"
OUTLINE = "盲目のハープ奏者を妻にもつ男性は、彼女が言う「月が見える」というのがよく理解できず、ちょっとした行き違いから喧嘩してしまう。"
THEME = "テーマ"
GENRE = "ヒューマンドラマ"
TARGET = "ターゲット（年代）"
SIZE = "8K"
CONTEST_INFO = ""
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
RELEASED = (9, 29, 2019)
MAJOR, MINOR, MICRO = 1, 1, 0


# Episodes
def ep1(w: World):
    return w.episode('1',
            Stage.no_sound_lady(w),
            Stage.soup_and_toast(w),
            Stage.helpmark(w),
            )

def ep2(w: World):
    return w.episode("2",
            Stage.kenka(w),
            Stage.her_concert(w),
            Stage.stop_music(w),
            Stage.break_them(w),
            )

def ep3(w: World):
    return w.episode("3",
            Stage.her_sound(w),
            Stage.her_and_moon(w),
            )

def ch_main(w: World):
    return w.chapter('main',
            ep1(w),
            ep2(w),
            ep3(w),
            w.symbol("（了）"),
            )


def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_released(*RELEASED)
    return w.run(
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

