# Developer and community statements on BF6 recoil and input (collected 16 October 2026)

Web search on 16 October 2026 for what DICE has said about recoil mechanics and mouse input, for the
recovery-law research (L4040 to L4047). Quotes are as reported by the cited outlets; the X posts were read
through the fxtwitter mirror. Nothing here is a decoded value; it is context for interpreting the captures.

## Developer statements

- **Florian Le Bihan (@DRUNKKZ3, principal gameplay designer), November 2025**, replying to a player's
  complaint that horizontal recoil made aiming sluggish: "I don't think it's a bug that we are looking at
  though, recoil essentially is 'added' to your aim input so if you move your aim against the recoil, it will
  feel more sluggish, if you move your aim with the recoil, it will accelerate it." Reported by GamesRadar
  (mirror: https://www.inkl.com/news/battlefield-6-s-recoil-is-making-aiming-so-inaccurate-players-want-it-fixed-immediately-but-lead-developer-suggests-it-may-be-a-skill-issue-i-don-t-think-it-s-a-bug-we-re-looking-at).
- **Le Bihan, 23 November 2025**: "We'll get it fixed, it's a pretty complex issue but we're already cooking
  some improvements that will help quite a bit with the issue until it's 100% fixed." Reported by GamingBolt
  (https://gamingbolt.com/battlefield-6-developers-have-been-cooking-some-improvements-to-fix-recoil-issues).
- **Le Bihan, 12 March 2026** (https://x.com/DRUNKKZ3/status/2032047272800719282), quoting NickelBF: "Nice
  video from @NickelBF showing that the way recoil and input now interface in BF6 is the same as how it did
  in previous BF games."
- **NickelBF (game designer, ex-BF4 competitive), 11 March 2026**
  (https://x.com/NickelBF/status/2031846180058001454): the absence of Apex-style recoil smoothing is not a
  bug and previous Battlefield games did not have it either; he datamined the VCR-2's recoil stats, converted
  them from polar to Cartesian and reimplemented them in a modified BF4, and the interaction with mouse
  movement "is exactly the same." Posted in reply to a player (@lql_00, 10 March 2026) claiming mouse input
  is overridden during tracking.
- **David Sirland (senior producer)** co-authored the Season 3 gunplay post
  (https://www.ea.com/games/battlefield/battlefield-6/news/bf-combat-gunplay): "we've done a wide pass across
  weapons to make recoil directions more consistent & predictable"; bullet deviation after the first shot was
  slightly increased; no statement on recovery or input. No post by "tiggr" on recoil mechanics was found.

## Patch notes that touch recoil and input

| Update | Date | Statement |
|---|---|---|
| 1.1.3.0 | 5 Dec 2025 | "Improved how recoil and aim input interact, resulting in more reliable accuracy when compensating for recoil." |
| 1.2.1.0 | 13 Feb 2026 | "Since launch, recoil compensation could feel inconsistent in certain situations ... the aim input required to counter recoil did not reliably match the recoil being applied." Now "recoil compensation has been made fully consistent, ensuring that the aim input required to counter recoil now correctly matches the recoil applied." Broad automatic-weapon recoil pass; "reduced recoil randomness" on B36A4, L85A3, M433, SOR-556 MK2. |
| 1.3.3.0 | 26 Jun 2026 | Recoil variation reduced across the arsenal; damage, dispersion and recoil variation adjusted. |
| 2.1.1.0 | 13 Oct 2026 | "Recoil Decrease Time Exponent on the SVDM and M39EMR increased from 0.75 to 1.1"; "Recoil Direction on the SVDM changed from 4° to 20°"; gamepad recoil compensation lowered from 11% to 5%; the SU-230 LPVO "no longer incorrectly reduces visual recoil" on six weapons. |

Sources: https://www.ea.com/en/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-1-3-0,
https://www.ea.com/en/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-2-1-0,
https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-2-1-1-0,
https://www.dexerto.com/battlefield/battlefield-6-season-2-patch-notes-3318907/, https://bf6balancelog.com/.

## Community thread, r/Battlefield, 14 July 2026

"[BF6] Why does nobody talk about recoil taking control of your input?" (u/MilliyetciPapagan, score 0; saved copy
in Datamining `reports\`). The poster, back from MW II, felt recoil "fake inputting" the mouse during full-auto
tracking. Nothing from a developer in the thread; the substantive replies:

- Several commenters point to the DRUNKKZ3 / NickelBF exchange above as the authoritative answer: recoil is
  applied on top of mouse movement, so a high horizontal roll against or with the mouse reads as under- or
  over-compensation; this is "working as intended", and what the complainers want is recoil smoothing
  (Apex-style), which DICE has declined.
- One commenter gives the mechanism in a line: "new camera rotation = old camera rotation + recoil + player
  input", and argues no shooter can do otherwise.
- Two commenters say something was wrong at launch and in 2042 ("360 test programs showed BF6's recoil affecting
  your input direction") and that it was fixed by the recoil patches (the 1.1.3.0 / 1.2.1.0 fixes above); one
  says their remaining complaint is "reticle bounce (visual recoil)".
- One commenter claims "the new update from 08/18/26 brought it back" (1.4.2.0 of 14 August 2026); unverified.

## What this means for the recovery research

1. The 2.1.1.0 notes name `Recoil Decrease Time Exponent` as a tuning operand, which confirms that the
   `RecoilDecreaseTimeExponent` field the site reads is the live recovery parameter and that DICE tunes
   sustained-fire controllability through it.
2. "Recoil is added to your aim input" and the 1.2.1.0 fix ("the aim input required to counter recoil now
   correctly matches the recoil applied") describe recoil as an offset applied to the player's aim in the
   same units as mouse input, which the recovery then removes. Before 1.2.1.0 the two did not match, so
   captures from before February 2026 are not comparable with current ones.
3. Le Bihan's endorsement of the BF4 reimplementation says the recoil-input interface is the BF4 one. The
   BF4 community model (Symthic) therefore applies to the interaction with input; it does not describe the
   recovery tail, which is what the 14 to 16 October captures measured with no mouse input at all.
4. "Gamepad recoil compensation 11% to 5%" is the controller auto-compensation (the site's controller int
   `94752c29` = 2 context, L4038); it does not apply to the mouse captures.
5. "Visual recoil" is treated by DICE as separate from applied recoil (the SU-230 LPVO bug), consistent
   with the camera-spring fields being cosmetic; the bullet-hole measurements bypass it either way.
