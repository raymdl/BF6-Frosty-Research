# Soldier mechanics

[Weapons](WEAPONS.md) · [Research queue](../working/FROSTY_RESEARCH_QUEUE.md)

This page records multiplayer soldier source configuration and display proposals. Serialized values, inferred meanings and effective match behavior are separate. Reads use 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`, except the [2.1.1.0 recheck (L4056)](#l4056---class-traits-training-paths-and-perks-on-2110-21-october-2026), which reads 2.1.1.0 (Head 5382784). Earlier receipts retain their original build and Head.

<!-- gunfight-L1103:start -->
## Selected handling settings and gunfight movement

[L1103](../../reference-data/provenance/frosty-2026-10-01-L1103-gunfight-handling-movement.json) checks M433 bare, Basic barrel with 30Rnd, and Basic barrel with 20Rnd. Named selectors, typed imports and table controls passed first. All 69 helper checks passed; 70 source reads include one preparation read. Retained 63-root evidence and 14 magazine/Basic-barrel chains were reused only after whole-file equality checks.

| Current software setting | Bare | Basic barrel, 30Rnd | Basic barrel, 20Rnd |
| --- | --- | --- | --- |
| ADS duration (ms) | 300 | 250 | 200 |
| Sprint recovery setting (ms) | 200.001 | 166.667 | 133.334 |
| Deploy setting (ms) | 633.334 | 533.334 | 466.667 |
| Holster setting (ms) | 233.334 | 200.001 | 166.667 |
| ADS movement ratio | 0.6 | 0.6 | 0.745 |

Selected source settings support these software values. The Basic barrel adds one ADS tier. Magazine catalog signs are the conversion of distinct source operations; they are not a universal modifier rule. Native ADS timing and composition, sprint firing readiness, and swap overlap/order remain unresolved. Deploy plus holster is not an established native swap total.

Named Jump_HorizontalVelocityCap `8` and Swimming_DiveSpeed `1.5` are structural configuration evidence. Their units and active consumers are unresolved. The site selects standing/moving spread; this does not prove a jump accuracy effect. StriderBF movement chapters supply a topic question only. The parent independently re-read SprintSettings_T06 offset `140` (`c1aa2a3e`, `0.16666699945926666`). No new correction or duplicate holster proposal is added.
<!-- gunfight-L1103:end -->

<!-- gunfight-ranked-soldier:start -->


## Ranked melee, ping and sneaking route qualification

[L745, L747 and L748](../../reference-data/provenance/frosty-2026-10-01-gunfight-ranked-soldier-qualification.json) inspected 17 exact current raw owners. Six structural GUID reads and a parent identity re-read passed. They are identity evidence, not mechanic controls.

| Question | Exact source boundary | Reopen condition |
|---|---|---|
| Melee damage and cadence (L745) | CombatKnife/shared-firing/SimEx/affector references reach `Struct_4df48d5e` and named delay expressions. The two payload field roles and attack timing remain unresolved. | Same-owner known-answer damage or cadence role and exact selected ordinary-hit/takedown receiver. |
| Ping timing (L747) | Messaging and ping callout bodies give identity/state channels. A reverse check of soldier input owners does not establish the danger double-tap classifier or voice-delay operand. | Exact named input-classifier or callout-delay consumer and separate known-answer timing control. |
| Sneaking audio (L748) | Enemy movement configuration imports the exact shared movement patch. State names do not supply a crouch/crawl attenuation quantity or radius. | Exact stance-to-audio receiver and same-owner known-answer gain/attenuation control. |

No damage, interval, combined ping latency, attenuation or audible-radius value follows. These are bounded route limits, not negative gameplay findings. The reverse input and exact audio recipient checks are recorded as method switches in the run.
<!-- gunfight-ranked-soldier:end -->

<!-- gunfight-fatal-precision:start -->
## Fatal-damage precision route qualification

[L742](../../reference-data/provenance/frosty-2026-10-01-gunfight-ranked-damage-qualification.json) checks the retained soldier health and healing-state routes. Their exact regeneration imports do not name the lethal comparison or its rounding operation. No death-threshold control was available. EA's reported near-99 case does not set a 99-damage death threshold. The site's epsilon arithmetic remains a software policy. Reopen with the exact damage-resolution caller and a known-answer lethal/nonlethal control. No negative gameplay conclusion follows.

### Kill threshold: firing-range tests (27 October 2026)

The operator ran firing-range tests on build 2.1.1.0, reading the on-screen damage number after each shot. Totals are computed from the site's Frosty damage values (stored as 32-bit floats; the 2-decimal site values reproduce them exactly) and the 1.4 / 1.57 / 1.8 headshot multipliers.

| Case | Hits | Computed total | Shown | Result |
|---|---|---|---|---|
| QBZ-192 Synthetic, 10 m | 2 head + 1 chest | 99.18 | 99 | no kill, next shot kills |
| QBZ-192 Standard, 50 m | 2 head + 3 chest | 99.35 | 99 | no kill, next shot kills |
| QBZ-192 Synthetic, 50 m | 1 head + 4 chest | 99.35 | 99 | no kill, next shot kills |
| AK-205 Standard, 10 m | 4 head | 99.34 | 99 | no kill, next shot kills |
| vz. 61 Standard, 50 m | 2 head + 5 chest | 99.53 | 99 | no kill, next shot kills |

- **Threshold:** no total from 99.18 to 99.53 killed. The site's kill-at-100 rule stands; a threshold in 99.53–100 is not excluded.
- **EA 1.4.3.0 note:** "Corrected an issue where a precise damage calculation could occasionally kill a soldier who had received roughly 99 damage." A community spreadsheet (SheetOnMyFace) recorded kills at 99.34–99.63 and modelled a 99.5 threshold; its tests predate this fix, so those kills are the fixed bug, not current behaviour.
- **QBZ-192 table:** the operator's 0/1/2-headshot BTK table for Standard, Hollow Point and Synthetic at 10–50 m matches the site exactly. The 75 m marker sits on the 75 m tier boundary; a re-run from just past 75 m matches the 14.62 tier (7/7/7, 7/7/6, 7/7/6).
- **Display:** the shown number is the running total, rounded as described in [UI_TEXT: hit indicator damage numbers](UI_TEXT.md#hit-indicator-damage-numbers-27-october-2026). The 99.53 case showed 99 because of the display rule, not a lower total.
<!-- gunfight-fatal-precision:end -->

<!-- gunfight-L1104:start -->
## Hit registration, suppression and flinch source boundary

[L1104](../../reference-data/provenance/frosty-2026-10-01-L1104-gunfight-native-consumer-limits.json) closes three named retained routes without a semantic control. Three current owner hashes and the cited site code hashes match. No numerical mechanic trace was launched. The review's missing-control flag is retained and accepted only as an audit of unqualified routes.

| Mechanic | Inspected source boundary | Required control and caller |
| --- | --- | --- |
| Hit registration | Soldier interaction callback, separate capsule/material context and the site's approximate target geometry. | Exact bullet/network event through authoritative hit acceptance and health commit, with an accepted/rejected-hit operation control. |
| Suppression | Exact Feature_Soldier_Suppression to PresEx_Suppression and compiled resource identity. Presentation ports do not qualify a health-regeneration effect. | Gameplay trigger/state to regeneration rate or delay operation, with a known-answer effect control. |
| Flinch | Exact animation hit-distance import and typed but unnamed projectile families. | Incoming-hit/near-miss caller to a typed gameplay aim/camera/weapon effect receiver, with a known-answer effect control. |

The site's target geometry, damage/BTK arithmetic and selected-ammo regeneration-delay addition are distinct software contracts. They do not establish these native effects. Creator suppression metadata cannot supply the missing source operation. No source/site correction is proposed. The named routes are exhausted within this audit; the effects remain unresolved, not absent.
<!-- gunfight-L1104:end -->

## Class, path and perk text (L840)

The current UI pass retains 155 text records: 17 class records, 12 training paths, 102 player abilities and 24 presets. Four class-name controls and 832 pointer/StringId checks passed. Each current raw hash equals L400; the earlier receipt retains Head 4892087. All records retain their exact object GUID, field path and type key. Four class records have explicit multiplayer context, nine records have explicit Granite context, and 142 remain ambiguous. A name shared by UI and gameplay is not an identity join. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L840-soldier-ui-atlas.json).

The complete text atlas includes suppression resistance, momentum, featherweight, combat recovery, stance protection and other entries outside the nine previously reviewed perks. These names identify questions for source tracing; they do not prove multiplayer availability or activation. The inspected metadata layout ambiguity remains recorded. Source text can support a perk information display after its class/path assignment is confirmed independently.

## Movement owner atlas (L841)

Three current owners were decoded: `GRX_Glacier_Soldier`, `Glacier_Soldier_Gameplay` and `GRX_Characters`. The initial L841 root families number 6, 15 and 4, with 223 nested field paths. L859 extends this initial inventory without changing its receipt. The known-answer jump-cap value 8 and dive-speed value 1.5 passed raw checks. The source scan keeps observed variants separate from registry bounds, whose outer-field roles remain provisional. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L841-movement-owner-atlas.json).

Exact release-ledger candidates connect sprint multipliers and slide thresholds to `SimEx_RootLayerLogic`, slide impulse to `SimEx_SlidingLogic`, and swim speed/acceleration to the swimming expressions. These caller joins require current raw checks. Normal walking, ladder, ADS and firing slowdown are still unresolved within these three owners. Prior jump/landing tuples remain configuration evidence. No effective speed or native equation is established.

## Survival owner atlas (L842)

Three current owners were decoded: `Glacier_Soldier`, `GRX_Glacier_Soldier` and `Glacier_Soldier_Spotting`. The exact regeneration-delay import and value 5 passed the control. The same soldier health owner imports baseline rate 10 and amount 0. Wrapper fallback zero is not the referenced value. Typed families and raw ranges are retained in the atlas. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L842-survival-owner-atlas.json).

Exact soldier imports expose health/healing-state presentation, revive trigger/stop logic and a ceramic-armor affector. This proves source references; it does not establish standard multiplayer armor or an effective revive time. The suppression feature and exact current PresEx target were captured and joined in L848; gameplay applicability remains unresolved. `GRX_Mutators` was an invalid brief route, so no absence claim follows. The prior receipt instead identifies `MutatorDatabase_CH1`, `SimEx_SetSoldierMutators` and `SimEx_SetSoldierModeSettings` for mode tracing.

## Class and perk owner atlas (L843)

All eight class path owners were examined, with 20 current owners and 13 exact import edge occurrences retained. The Recon_1 slot 0 GUID control matches the AdvancedSpot Ability export. The FasterRegen affector control reproduces rate/delay/amount 30/2.5/0. A separate AdvancedSpot registry value 1.33 does not establish a direct Ability-to-registry import. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L843-class-perk-owner-atlas.json).

StanceFlak and Featherweight current selections were traced in L847/L850/L852/L854; other exact path-selected targets remain open. UI/gameplay identity and native effects retain their own limits. Hash-only fields have no invented numeric roles. Import order is not an unlock level; UI-to-gameplay identity and active multiplayer selection remain unresolved. The atlas retains every scoped path edge and the exact reopening condition for each missing route.

## Soldier field atlas and coverage (L844)

The [summary receipt](../../reference-data/provenance/frosty-2026-10-01-L844-soldier-field-atlas.json) retains `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T001825-0400-soldier-frontier\soldier-atlas.json` with 29 unique inspected owners, 423 owner-family entries and 155 UI records. The mechanic classification covers 34 groups: {'modeled': 8, 'traced not on site': 8, 'known limit': 13, 'never examined': 5}. Family entries can overlap between bounded owner passes. Every inspected family keeps its type identity, fields, observed variants and artifact provenance. This is a bounded field atlas; the multiplayer owner frontier was still open at this pass. [L866](#current-source-coverage-and-run-closure-l866) later closed controlled exploration: 18 known limits, none never examined.

The site currently models ADS movement multipliers, sprint recovery, deploy/holster ladders, health-target input, regeneration delay and fire-detection ranges. It does not establish their native composition. Remaining work starts with firing slowdown, stance speeds, ladder transitions, revive/regen consumers, class selection, suppression and mode settings. The current control and parent raw rereads passed.

The official [Season 5 preview](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-community-update-siege-of-vegas-incoming) places training-path revisions and faster armor application in its Battle Royale section. No specific multiplayer soldier numeric change is stated there. Shared Common path/affector assets needed a multiplayer recheck after the update; the 2.1.1.0 recheck ([L4056](#l4056---class-traits-training-paths-and-perks-on-2110-21-october-2026)) found the path assets and multiplayer stored values unchanged. Announced BR effects are excluded from current MP proposals.

L845 movement expression receivers (1 October 2026)

All four current source owners resolve Class_53d7404d with exact root key68be6a6ba6ab0bcbd19fd6d9bb5f89fb. Known Jump and DiveSpeed raw controls pass. Both swimming owners exactly import the known DiveSpeed export. The scoped pass retains20 registry settings and no native equations.

RootLayerLogic imports FastSprintTopSpeedMultiplier and DefaultStandSprintTopSpeedMultiplier at compiled input80/81. Source slots are2.05 and1.857. Exact named CurrentStance, TargetStance and FastSprintRequired channel exports add state context. No normal stance speed or tactical-sprint formula follows.

A new named Float FiringMoveSpeedMultiplier declaration points to unexported local43, Class_829b82ea, initialized to1. The raw pointer at9912 is -6936 and resolves local start2976. No direct Commando import was found in the four expression import tables. This local is an exact next route for a Commando channel/output comparison, not a quantified firing penalty.

RootLayerLogic imports slide accumulating time0.25, needed velocity5.2 and cooldown1. SlidingLogic imports Slide.ImpulseLength25. Both swimming expressions import ten same named scalar settings, including swim velocity3.33, sprint velocity7.65 and acceleration gain0.05. Legacy also imports FreeDiveEnabled false. Units, receiving equations and active branch remain unresolved.

Each root selects an exact compiled object and resource: Root2bfca9f18b8f10e9; Slidinga39a2d6b9590ffcd; Swimf8e2e938b5253bf5; Legacyb8298cca4c1481c1. ResourceRef bytes are checked. Existing reader documentation establishes a bounded tooling limit. L853 has current same-Head bytes for seven exact resources. Obtain a known-operation reader before interpreting equations; bytes alone do not resolve grammar.

No numeric site proposal follows. The site's ADS movement ratios and sprint recovery timing are separate models. A conditional qualitative Agile Shooter tooltip is supported by the supplied EA guide and existing UI text; require current exact perk identity before adding it to a selected class. No capture, repo edit or compiled grammar parser was performed.

L846 source frontier

Control passed. New source facts: healing state expression imports HealthIsHealing; revive trigger imports named team/squad ability and request channels; revive stop imports request/player/health channels. AffectorRevive_Regen uses RegenerationRate, PostRevive_RegenerationDelay and RegenerationAmount in the same role slots as the reviewed baseline. Hash-only tail fields do not prove interruption. Fall affector has exact damage-definition imports; nested layout is ambiguous, so numeric slots remain unnamed. See l846-result.json nextRoutes.

Existing expression resource review has no operation grammar. No effective regen composition/reset, revive health, fall threshold or native activation claim. EA guide context supports qualitative display proposals with controlled manual health-HUD comparisons, without recordings.

L847 controls passed. Five effect groups examined. Current exact source selection extends StanceFlak and Featherweight routes; Commando, Support sprint exemption and WeaponSwap retain specific receiver limits.

Support_2 slot1 -> current Ability_StanceFlak -> current FL -> exact expression import; affector semantics require a same-owner role control.
Assault_1 slot1 -> current Ability_Featherweight. Ability exposes exact U selector import but no scoped FL/affector payload. Soft Landing guide/UI text does not establish gameplay UI identity.
Assault_2 slot1 -> current Ability_Commando_Base -> exact U. Named current FiringMoveSpeedMultiplier storage1 has no exact Commando channel join.
WPM_SupportTrait exactly selects ADS Anim/FOV children with Field_9540bd8e +1 each. This inspected family does not establish a sprint exemption receiver. A 4 October 2026 census of 35 current `_BaseTraits` assets ([receipt](../../reference-data/provenance/frosty-2026-10-04-base-traits-value-census.json), Head 4909067) found no sprint multiplier and no weapon-class or LMG selector: the sprint and crawl affectors are scalar-free identity records, the only operands are identity transforms, neutral 1.0 multipliers and unrelated healing, overheat and regeneration values, and none of the 27 imports is a Soldier/Features asset. This is absence within those assets, not a finding that no LMG sprint penalty exists.
WM_WeaponSwap retains selector7727fe65-6ddd-4d10-aeb8-e2d1e59c9054 and Class_4aac041b.Field_9540bd8e +1. Prior draw-step interpretation is retained as context; current selector owner/receiver and swap totals remain unresolved.

EA class guides support their own text and unlock levels, independently of UI/gameplay mapping. Duplicate ActiveFlak description identities remain separate. No new additional-family numeric interpretation or native formula is established.

L848 extends the soldier atlas with exact Feature_Soldier_Suppression → PresEx_Suppression and current named spotting/suppression/mode setting definitions. PresEx member names are presentation structure, not gameplay effects. The spotting owner imports BR shakedown/spectator variants; exclude these from standard MP claims. SimEx mode inputs include GameMode, GameState, IsSP, IsQuickRespawn, HasModeTweaks, IsGranite and IsGauntlet. Mode root properties remain timeout-specific. Keep health/damage multipliers and revive/death defaults separate from active overrides. Reopen only on exact caller input values and a supported compiled-resource evaluator with same-owner control. Proposals and non-recording validation predictions are in l848-result.json.

L849 weapon movement and handling selections

All63 current WB raw hashes match the authoritative prior receipts. Current u32 rereads reproduce all ADS, sprint and DTA selections. The independent named ADS control uses the M433 owner/schema, exact registry wrapper, and child/hash pair.193 scalar reads stay within the200 cap.

| Weapon class | Count | ADS base ratio | Default sprint ms | Default deploy ms | Default holster ms |
|---|---:|---:|---:|---:|---:|
| Assault Rifle | 11 | 0.6–0.6 | 166.667–166.667 | 533.334–533.334 | 200.001–200.001 |
| Carbine | 9 | 0.67–0.67 | 133.334–133.334 | 466.667–466.667 | 166.667–166.667 |
| DMR | 6 | 0.475–0.67 | 133.334–233.334 | 466.667–733.334 | 166.667–266.667 |
| LMG | 10 | 0.475–0.535 | 200.001–266.667 | 633.334–866.667 | 233.334–300.001 |
| SMG | 10 | 0.745–0.745 | 100.001–100.001 | 400.001–400.001 | 133.334–133.334 |
| Shotgun | 4 | 0.6–0.67 | 133.334–166.667 | 466.667–533.334 | 166.667–200.001 |
| Sidearm | 7 | 0.745–0.825 | 66.667–100.001 | 200.001–350.001 | 83.334–166.667 |
| Sniper Rifle | 6 | 0.42–0.67 | 133.334–233.334 | 466.667–633.334 | 166.667–233.334 |

The table shows current site model ranges. Do not use class averages as source selectors. VZ61 retains the primary DTA table despite its Sidearm class. Deploy and sprint coordinates are independent.

M433 source bases select ADS 0.6, sprint 200.001 ms, deploy 633.334 ms and undeploy 233.334 ms. Its default 30 Rnd magazine shifts sprint and deploy by -1, so the current model displays ADS 0.60×, sprint 167 ms, deploy 533 ms and computed holster 200 ms. Existing UI cards already display the first three. A separate Holster setting card can show the fourth, with a source-setting label.

A non-recording model check is saved: selecting M433 20 Rnd gives ADS 0.75×, sprint 133 ms, deploy 467 ms and holster 167 ms with actual UI formatting. These are software predictions, not gameplay measurements.

Absolute ADS m/s speed requires an exact soldier baseline and equation. Total weapon-swap time requires animation/state sequencing and overlap proof. Do not multiply unresolved soldier tuples or add holster and deploy as an effective swap duration. Prior table operands are carried through equal current hashes; they are not reported as new measurements.

L850 source frontier

Controls passed. Six fall U selectors resolve bc0062dc roots and e923016e local lists. Their outgoing imports target CT_GLA_CH1_S0_Common file18958c64-77e6-6301-9a22-738608045d48. Mid/High share one child; ManDown/Death share one child. This does not prove equal effective damage.

Assault_1 slot1 -> Ability_Featherweight -> exact U_Ability_Featherweight is current and raw-checked. Ability local CT child df766bf5 differs from U child0bf78e74. These exact CT children are next routes; no direct landing/jump numeric receiver was decoded under the 12-owner cap. EA Soft Landing wording supports only a separate qualitative proposal.

L851: StanceTransitionLogic selects exact TargetStance, TransitionInputBlock, ReviveState and CurrentAction channel GUIDs, registered ProneAllowed_PerTeam defaulttrue, and named TransitionInputBlockTime tuple. ProneLogic exposes WasSprinting state. UpdateLadder exposes findLadder function names and exact compiled resource06f5831872e5c30d. All match the current RootLayerLogic expression type key; active caller selection is unresolved. L132/L134 jump/landing tuples carry forward without new units/equations. Soldier object80 imports animation FB.Hit.Distance.Float; retain as presentation only. Object81/87 local typed numeric families remain hash-only. Do not derive gait/flinch values from them. Exact next routes are in l851-result.json.

L852 controls passed. Four fixed mechanisms examined within16 current owners.

StanceFlak current affector payload is0.75/true/false/false, with root enum3. All roles remain hash-only; FasterRegen is a different family and projectile hash names do not transfer.

Current UI object217 identifies Evasion Training. Object421 identifies Heavy Flak. Duplicate ActiveFlak object36 identifies Rally Squad. No exact gameplay identity join is proved.

Current Recon_2 slot2 selects LowProfile Ability ->U/FL->SimEx. Its exact imports include CommandingPresenceRegen alongside SpotDelay/SpotDuration and CurrentStance. Engineer_1 slot0 selects EngineerBase, but this does not map the guide signature trait. Finished Engineer hip and Recon sway evidence is reused without new inventory.

Current soldier armor reference and Conquest/Breakthrough caller roots do not establish MP armor applicability. Gadget internals remain excluded.

### L853: compiled soldier equations

Seven `SerializedExpressionNodeGraph` bodies are captured on Head4909002 and paired with exact current EBX resource operands: root movement, slide, both swimming variants, suppression presentation, soldier mutators and mode settings. The resource sizes range from1856 to309904 bytes. Raw RID/preamble checks pass. The inspected local source has a resource type enum and generic metadata handling, but no qualified operation evaluator. The [public ResourceRef source](https://github.com/FrostyToolsuite/FrostyToolsuite/blob/master/FrostySdk/Ebx/ResourceRef.cs) describes resource identity only.

This closes the prior mixed-Head pairing gap for these seven bodies. It does not establish speed equations, interruption gates or active mode values. Reopen with a reader or independently validated operation control. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L853-soldier-resource-reader.json).

L854 source finding

Control passed. Six exact CT children resolve same-owner names and configuration addresses. Fall labels are Fall_Damage, Fall_Low_Damage, Fall_Medium_Damage and Fall_Death_Damage. Featherweight Ability CT child is named U_Ability_Featherweight; Featherweight U CT child is named U_Ability_FasterHealing. This mismatch is a serialized association, not proof of an active FasterHealing effect or game bug.

CT root inherited Field_6bd9ee7d imports the exact current value registry. Selected Field_ffba60f0 positions return to the same CT exported children. This completes the address loop; it establishes no numeric damage, landing effect, activation or native threshold. Next route requires a qualified execution consumer, not another inventory.

L855 gap audit: keep the soldier frontier open. The 32 exact class slots select 28 distinct Ability targets. Twenty targets still need downstream source/effect classification. Current path GUID controls qualify those source continuations. Names alone cannot exclude gadget, vehicle or BR effects, or join a UI label to behavior. The initial atlas count of 29 owners and 13 selected edges is a stage snapshot. Completed L845-L854 passes supersede older capture-gap and never-examined states. Their native role and compiled limits remain. L853 has current resource bytes but no qualified operation reader. frontier-rank.json supplies all exact targets, existing controls, reserved L856 routes, atlas extensions and surgical SOLDIER.md corrections.

L856 controls passed. Four fixed rows,12 current owners.

LowProfile exact SimEx target CommandingPresenceRegen matches the current FasterRegen root and payload descriptors. Source roles are rate -1, delay3.5 and amount -1; references are null. Negative sentinel meaning and effective composition remain unresolved.

SpotDelay stores1.2. SpotDuration stores0/0.667 plus three uint32 selector codes. Exact named baseline or receiver slots are not found in the two scoped baseline owners; no duration/multiplier interpretation is made.

Engineer Ability selects its exact U, KST59 and CT4475. U selects CT4345 named U_Ability_FasterHealing. These config wrappers are not effect bodies, and stored KSTfalse is not a proved active disable. Signature soldier resistance mapping remains unresolved.

# L857 Assault and Support Ability source frontier

All nine current class-slot selections pass exact file/export checks. Each selected Ability configuration resolves a named CT child and an exact registry round trip. No numeric soldier effect follows from this loop.

| Source Ability | CT name | Registry address |
|---|---|---|
| Ability_SpawnAdrenaline | U_Ability_SpawnAdrenaline | 5234 |
| Ability_ActiveAttack | U_Ability_ActiveAttack | 5208 |
| Ability_Grenadier_Base | U_Ability_Grenadier_Base | 3300 |
| Ability_AssaultGadgetReload | U_Ability_AssaultGadgetReload | 3305 |
| Ability_MedicalTriage | U_Ability_MedicalTriage | 1124 |
| Ability_ReviveHealthRegen | U_Ability_ReviveHealthRegen | 4673 |
| Ability_PerimeterDefense | U_Ability_PerimeterDefense | 822 |
| Ability_ActiveMedic | U_Ability_ActiveMedic | 3314 |
| Ability_CrateResupplyPlus | U_Ability_CrateResupplyPlus | 5250 |

ActiveAttack and ActiveMedic also select exact FL targets. The fixed body bound leaves these execution bodies and the U bodies for a separate bounded stage. All root layout ambiguities remain explicit; unrelated decoded scalar fields have no claimed roles.

The official [Assault guide](https://www.ea.com/games/battlefield/battlefield-6/news/assault-class) and [Support guide](https://www.ea.com/games/battlefield/battlefield-6/news/support-class) support separate qualitative class guidance. They describe grenade and gadget effects independently. The source address loops do not prove a UI-to-gameplay mapping.

No numeric site correction is proposed. Native activation, readiness, health, movement and runtime composition remain unresolved.

L858 complete within the source scope:10 mechanism rows,36 owners. Controls and exact slot/export joins passed. Six SimEx bodies bind compiled resources and exact outgoing members; no effective numeric soldier values are claimed. Next routes retain affectors and soldier registry children. Runtime activation and graph grammar remain unresolved. No site changes, recordings, captures, or Git writes.

L859 reviewed complete. Four structural rows; controls pass. 118 selected non-weapon owners: 104 inspected, 14 captured only. 1580 typed family entries. 23816 numeric observations match 35055 unique physical reads. All32 slots and28 targets pass92 export/import reads. Value-registry retains 25 previously scoped positions; 79 existing raw reads reused. Combined original UI inventory is 122 distinct owners. Original stage1 atlas unchanged. L858 result pending at the pinned snapshot. No site changes or native claims.

Use soldier-atlas-frontier-v2-reviewed.json as the reviewed structural snapshot. Keep14 captured-only exact body gaps and downstream source/native limits open.

# L860 Assault and Support source effects

Nine U and two FL routes pass exact current identity checks. Eight U wrappers select the shared FasterHealing configuration at address422. ReviveHealthRegen selects Triage at address3529. These are source configuration addresses. They do not define healing magnitudes.

ActiveAttack and ActiveMedic select exact compiled source graphs. Their resource IDs are a94df18e953338b1 and196e489adbfbb9b5. RootTransform, SquadId and TeamId are exact contextual channel names. Binding order, conditions and native execution remain unresolved.

The selected Affector_ActiveMedic and shared Affector_FieldUpgrade_Ulti_Consumed use Class_6bbe0eba. Its schema differs from the controlled FasterRegen family. No rate, delay or amount role transfers. ActiveMedic token2485301187 matches its selected source graph token; that is an identity join.

SupplyCrate, MedicCrate, AmmoCrate and AdrenalineShot hardware branches stop at exact source/export boundaries. No hardware affector body is decoded and no exclusive applicability claim follows.

The official [Assault guide](https://www.ea.com/games/battlefield/battlefield-6/news/assault-class) and [Support guide](https://www.ea.com/games/battlefield/battlefield-6/news/support-class) can support separate qualitative class descriptions. No numeric weapon or soldier model change is supported by this pass.

## Source limits and display proposals (L861)

The first dead-end batch retains 14 exact route limits with the inspected fields, work done, stop reason and reopening evidence. A source limit means that the inspected route lacks a qualified next operation or role control. It does not mean that the multiplayer effect is absent. Residual class effect and spotting routes remain open in L860/L862/L863, and L864 updates the atlas.

The queue now has six proposals: the existing model's holster setting, plus guide-supported Quicker Recovery, Soft Landing, Revive Recovery, Explosives Resistant and Low Profile descriptions. Each proposal has a concrete prediction. Only the holster proposal has a validated software number: M433 30 Rnd gives 200 ms and 20 Rnd gives 167 ms. Source handling settings do not establish total swap time. Perk text can state the official guide effect after current UI selection verification; unresolved raw operands do not supply additional effective values. The operator parked the five perk-description proposals on 1 October (research only; the site has no class/perk surface), so only the holster proposal remains live.

The Season 5 preview describes its training-path changes within battle royale. Shared Common owners needed an MP overlap check after the update; [L4056](#l4056---class-traits-training-paths-and-perks-on-2110-21-october-2026) found them unchanged on 2.1.1.0. No specific MP numeric change is asserted. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L861-limits-proposals-batch1.json).

L862 complete: exact spotting-to-OverlayPicker receiver qualified after the suppression PresEx positive control. Five presentation ports, local InLobby/Active states, and exact outgoing imports are retained.39 stored f32 values are raw checked but do not establish effective durations or ranges. Four owner files inspected. Multiplayer branch selection, native activation and gameplay detection remain unresolved. No site changes.
Current collection catalog resolves23 of27 outgoing import occurrences. Four occurrences across3 file GUIDs remain catalog gaps. Existing raw paths/hashes and same-owner control guidance appear in next-routes-v2.json. Use draft-receipt-v2.json and l862-result-v2.json.

L863 completed the fixed seven-row source scope. The independent FasterRegen control reproduced rate 30, delay 2.5 and amount 0. All eight incoming edges and target exports passed raw checks.

AntiRepair, ActiveRepair and Ulti_Consumed share a hash-only typed family. MechanicOverheat Stationaries/Vehicles share another family with false plus 0.5/0.9; these values have no qualified effect role. The two exact GRX children retain named scalar storage: Mine Sweep Radius 30 and DamageSpot_Duration 8. Units, tuple companions and native operations remain unresolved. No hardware exclusion or gameplay formula follows.

Eight bodies were decoded. Incoming SimEx receipts were reread at selected fields only. No vehicle/gadget bodies, captures, repository changes or site changes were made. No generated output exceeds 50 MB. See family-atlas.json, raw checks, next-routes.json and draft-receipt.json.

L864 complete. Controls pass. 132 scoped owners (136 with original UI owners), 1899 typed families and 25243 numeric observations. All14 captured-only body gaps close. All32 slots/28 Ability targets retain source dispositions. Canonical L860/L862/L863 integrated. 476 new physical reads; 1088 extension reads reused. No source role or native activation inferred. L865 was then pending (27 outgoing occurrences and 3 file-GUID index gaps; completed below). Original and L859 atlas snapshots unchanged.

Use soldier-atlas-frontier-v3.json for this snapshot. Source closure is separate from native meaning. At this snapshot the L865 exact selected receiver pass stayed open and the frontier was not labelled exhausted; L865 and [L866](#current-source-coverage-and-run-closure-l866) closed it.

L865 complete:3 groups,12 target files,19 exact selected exports. Same-owner RegenerationDelay5 control passed. Seven soldier overlay names, SP_Squad Overlays Enabled, WaterState/HallucinationAmount and six own option names qualified. Seven f32 values raw checked; overlay scalar50 is not gameplay spotting range. Palettes and PsyGas descriptor/name only. Three missing file GUIDs remain catalog limits. Native MP activation and compiled equations unresolved. Exact killswitch/WaterState enum next routes retained. No site changes.

## Current source coverage and run closure (L866)

The available source frontier now has no unvisited in-scope target with an exact current body and a passing control. This closes controlled source exploration; effective native mechanics remain partly unresolved. Three exact OverlayPicker file identities are absent from the current catalog. They remain index limits, not asset-absence claims. A new file identity, named role/consumer control, or validated compiled-operation reader can reopen the recorded limits.

The core atlas contains 132 inspected non-weapon owners, 1,899 typed families, 25,243 numeric observations and 36,622 physical reads. Four initial UI owners give 136 core/UI owners. Selected presentation supplements are counted separately. All 32 class-path slots and 28 Ability targets have exact selection and downstream source dispositions. All 14 captured-only inventory gaps closed. The 34 requested mechanic groups are 8 modeled, 8 traced not on site and 18 known limits; none retains a never-examined classification within this controlled scope. Global registries and hardware boundaries retain explicit partial coverage.

| Area | Established source/display evidence | Remaining native or role limit |
|---|---|---|
| ADS and handling | All 63 weapon selectors match prior raw hashes; current magazine model reproduces ADS, sprint, deploy and holster settings. | Absolute stance/ADS speed and total swap/readiness sequence. |
| Movement, jump and landing | Exact named sprint, slide, swim, stance and ladder inputs; current Jump cap 8 and Dive speed 1.5 controls. | Composed speeds, acceleration, thresholds and active compiled equations. |
| Health and recovery | Baseline regen roles 10/5/0; FasterRegen 30/2.5/0; LowProfile receiver -1/3.5/-1 in the matching family. | Units, sentinel meaning, reset, stacking and timing. Never display negative healing from -1. |
| Revive and fall | Exact request/state roles and fall/Featherweight configuration loops. | Gate order, revive duration, effective damage/landing thresholds. |
| Class paths and perks | Every selected Ability and in-scope captured body classified; StanceFlak source 0.75, DamageSpot_Duration 8 and Mine Sweep Radius 30 retained with roles/limits. | UI/gameplay identity for Evasion Training/Heavy Flak; damage role of 0.75; units and active effect operations. |
| Detection and reactions | Exact suppression/overlay presentation receivers, named channels and option/enum definitions. | Gameplay spotting range/duration, suppression/flinch mechanics and active MP branches. |
| Armor and modes | Exact soldier armor import and named mode inputs/defaults. | MP armor enable/caller and selected combat overrides. |

One queue proposal remains reviewable, the holster setting; the five official-guide perk descriptions are parked (operator, 1 October; the site has no class/perk surface). M433 30 Rnd predicts holster 200 ms; 20 Rnd predicts 167 ms. Each proposal has a non-recording validation prediction. Guide descriptions require current UI selection verification before binding. The Season 5 preview puts training changes in battle royale; the 2.1.1.0 recheck ([L4056](#l4056---class-traits-training-paths-and-perks-on-2110-21-october-2026)) found the shared Common path assets and MP stored values unchanged.

Two evidence-reference corrections are explicit: the L840 preliminary atlas survives under its preliminary filename; L855's mutable topic-page hash is historical and lacks an exact retained snapshot. Immutable raw/source results support the final coverage. No old receipt was changed. [Closure receipt](../../reference-data/provenance/frosty-2026-10-01-L866-soldier-frontier-closeout.json).

## Final spotting option and enum boundaries (L867)

Seven exact imports from L865 select five reset entries in two CH1 tables and the WaterState enum. The reset entries name HUD, soldier overlays, color-blind mode and spectator outlines; one outline-strength import selects `OptionJoystickDeadzoneCenter_Reset`. This is a source identity mismatch, not evidence of joystick effects. Their actual Int registry family differs from the controlled EngineerBase Bool family. Each stores 0 with tuple companions 0 and 31. No Bool switch meaning or active MP assignment transfers.

The exact `WaterState` channel selects `MM.WaterState.Enum`; its five local member definitions are raw checked. These definitions do not evaluate the compiled OverlayPicker conditions. The three unresolved OverlayPicker file GUIDs remain index limits. No gameplay spotting range or numeric site change follows. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L867-spotting-option-enum-boundaries.json).

<!-- native-semantics:L1001:start -->
### Exact descriptor enum reader (L1001)

Exact descriptor enum membership is available through the L1001 reader. Current atlas application adds no zeroing, stance/state, spotting or vehicle enum names. Hash members stay unnamed. See the [receipt](../../reference-data/provenance/frosty-2026-10-01-L1001-descriptor-enum-reader.json) for identity counts, controls and limits.
<!-- native-semantics:L1001:end -->

<!-- native-semantics:L1002:start -->
### Curve and table reader boundary (L1002)

The L1002 reader identifies exact controlled curve/table schemas in the current atlas. Site-model interpolation controls do not name physical axes or native interpolation in other owners. No atlas semantic meaning or site number changes. See the [receipt](../../reference-data/provenance/frosty-2026-10-01-L1002-curve-table-reader.json) for identity counts, controls and limits.
<!-- native-semantics:L1002:end -->

<!-- native-semantics:L1006:start -->
### Authored local-state enum boundary (L1006)

Current named local objects use `Class_3038efcc.Field_b6657270` as exact enum descriptor 852, hash `3a012691`. InLobby stores 0 and Active stores 1 in OverlayPicker. Other exact current owners contain multiple distinct authored names with the same value: mode settings have ten names at 0, mutators have four at 0, and the NVG filter has RawAlign and NVG at 1. Independently controlled type and raw reads pass. The proposed unique state-ordinal control fails: that route is wrong. No semantic absence claim follows from it. Keep the enum role unnamed; these values are not qualified global stance/state IDs or compiled state transitions. No reader or atlas semantic promotion is made. See the [receipt](../../reference-data/provenance/frosty-2026-10-01-L1006-authored-state-enum-control.json).
<!-- native-semantics:L1006:end -->

<!-- native-semantics:L1008:start -->
### UI choice/value enum boundary (L1008)

The final enum method tests exact retained UI choice/value bindings. Current widget-to-zeroing DBD pointers, exported GUIDs and local keys pass the source identity control. The selected enum 536 UI array is empty, and its retained UI text list has zero records. Five selected spotting reset entries store exact INT32 values 0, 0 and 31; they are not established named enum choices. No complete named UI choice/value mapping exists in the inspected selected artifacts. This scoped limit does not establish absence elsewhere. Missing contracts and exact reopen conditions are in the two result rows. No zeroing or spotting enum meaning is promoted. See the [receipt](../../reference-data/provenance/frosty-2026-10-01-L1008-ui-enum-binding-control.json).
<!-- native-semantics:L1008:end -->

## L4056 - Class traits, training paths and perks on 2.1.1.0 (21 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-21-L4056-class-perk-recheck-2110.json). Full per-slot table: `BF6 Datamining/reports/weapon-analyzer-research/2026-10-21-class-perks/perks-2110.md` (SHA-256 `fb67e6cf…`).

What was compared: the 1.4.3.5 pre-update capture against the 2.1.1.0 capture, each decoded with its own descriptors and read with its own English string table.

- **Unchanged:** the four class/path/perk UI metadata assets (same bytes as L400 and L840), all 16 `FieldUpgradePath_*` and `U_FieldUpgradePath_*` assets (eight multiplayer paths, four slots each, same order), and every stored affector scalar reached from the 32 multiplayer slots (FasterRegen 30 / 2.5, StanceFlak 0.75, MechanicOverheat 0.5 / 0.9, LowProfile 0.667 and CommandingPresenceRegen 3.5). Of 61 byte-changed `InRoundProgression` assets, 59 differ only in compiled type indices, body hashes, resource ids and a new affector header field `Field_492c22c3` = 3. The 29 captured graph bodies hold the same constants as the 10 October listings. The Season 5 training-path revisions announced for Battle Royale leave the multiplayer path assets untouched.
- **Flak:** `Ability_Flak` now imports a new `Affector_FlakJacket` (0.67, explosive) instead of `Affector_Flak` (0.67, explosive); the value is the same. `Affector_Flak` is still imported by the Engineer Mechanized Infantry graph. The perk text gained "increased by 33%", which matches 1 - 0.67.
- **Quick Plating (Battle Royale Pointman path):** text changed from "33% faster" to "25% faster" (string `3EA804EE`), but the `SimEx_Ability_Pointman_Base` and `SimEx_FasterArmorReplate` bodies still store 1.5 with the stat id in call `239dc415` moving from 34 to 35. Where the 25% is set is open; this perk is not on a multiplayer path.
- **Recon class record:** `Field_aff0eb51` / `Field_59ba3119` now resolve to "AIM-SPOT" and the aim-down-sights spotting paragraph, the same fields that hold MISSION FOCUSED (Assault) and MECHANIZED INFANTRY (Engineer). The Support record's two trait strings are still missing from the English table, and the `Ability_ReconSniper_Base` ("Passive Spotting") perk record lost its strings in the same table change.
- **Catalog:** new affectors Bombardier, FlakJacket, MoralSupport, Reciprocity and four `ReservesF2P` redeploy-ammo affectors; removed EnhancedFiltering and GasReveal graphs, ImprovedTargeting, the HemostaticSmoke `U_` asset and the PrepperBase trio (all Battle Royale or gas-mask content). Soldier registry: one row added (`ArmorGrantSpawnPlate`), none changed.

Multiplayer path slots and their UI text on 2.1.1.0 (slot order as stored; the `_1`/`_2` path to UI title join is not stored, the loadout presets `MP_<class>_1/_2` carry the same titles):

| Path | Slot 0 | Slot 1 | Slot 2 | Slot 3 (active) |
|---|---|---|---|---|
| Assault_1 | Adrenaline Rush | Soft Landing | Quick Recovery | Rally Squad* |
| Assault_2 | Extra Grenades | Agile Shooter | Unrelenting Reload | Rally Squad* |
| Engineer_1 | Extra Rockets | Launcher Proficiency | Devastating Impact | Thermal Overdrive |
| Engineer_2 | Gadget Fortification | Overheat Control | Mine Detection† | Thermal Overdrive |
| Recon_1 | Enhanced Perception | Target Acquired | Confirmed Kill | UAV Overwatch* |
| Recon_2 | Stealth Tactics* | Gadget Awareness‡ | Low Profile | UAV Overwatch* |
| Support_1 | Urgent Aid | Revive Recovery* | Defense-Focused | Restock Allies |
| Support_2 | Logistics Expert | Explosives Resistant | Steady Aim | Restock Allies |

\* UI record found by its text, not by internal name (the record's internal name differs: Ability_ActiveFlak, Ability_ActiveUAVCallin, Ability_ConcealedRescue, Ability_CrateHealPlus). † Internal name differs by case only (`Ability_Mechanic_base`). ‡ Matched by display name; the record's internal name is `Ability_PathfinderBase`. None of these is a stored join (L840).

Open: a stored UI-to-gameplay join; which UI path title is `_1` and which `_2`; the consumer of the Quick Plating speed; why `Affector_Flak` was duplicated rather than edited.

## L3309 - Spotting and detection registry values (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3309-spotting-detection.json). Dataset: `reference-data/frosty/registry-spotting-detection.json` (212 rows, each default read back at its raw offset). These are registry defaults from `GRX_Glacier_Soldier`; meaning is read from the row name, and units and use in a match are unconfirmed.

| Row | Default | Min | Max |
|---|---|---|---|
| `TimeToSpot` | 0.5 | 0.1 | 3 |
| `SpottingFoV` | 7.5 | 2 | 55 |
| `SpottingDistanceHip` | 10 | 5 | 30 |
| `SpottingDistanceZoom` | 100 | 15 | 300 |
| `SpottingDistanceVehicle` | 100 | 0 | 999 |
| `HipfireSpottingEnabled` | false | | |
| `DefaultSpotDuration` | 5 | 1 | 60 |
| `SpotDuration` | 2.5 | 0 | 0 |
| `VehicleSpotDuration` | 30 | 1 | 60 |
| `GadgetSpotDuration` | 20 | 1 | 9999 |
| `DamageSpot_Duration` | 8 | 0 | 100 |
| `SpotOnFireDuration` | 0.4 | 0.1 | 10 |
| `AdvancedSpotRangeMultiplier` | 1.33 | 1.1 | 1.5 |
| `AdvancedSpotAngleMultiplier` | 1.1 | 1.05 | 1.25 |
| `AdvancedSpotBaseTime` | 0.25 | 0.1 | 1.5 |
| `AdvancedSpotDurationIncrease` | 3 | 0 | 7 |
| `TrackerBaseSpottingDurationMulti` | 1.25 | 1 | 10 |
| `TrackerBaseSpottedDurationMulti` | 0.66 | 0.001 | 1 |
| `AmbushTrainingSpotResistance` | 4 | 0 | 8 |
| `ThermalSignature_Standing_Min` / `Crouched_Min` / `Prone_Min` | 0.5 / 0.25 / 0.1 | | |
| `IntelUpgradeSensorRadiusMultiplier` | 1.5 | | |
| `ImprovedJammerRadiusMulti` | 2 | | |

`GRX_Characters` also stores drone and sensor rows (`DroneControlledSpottingCylinder_*` height 100, top radius 12.5, spot duration 6, cycle 0.35; `MovementSensor_Radius` 25; `Pulse - Radius` 60). That registry also holds rows named for earlier-game specialists, so these may be leftovers; they are in the dataset but should not be read as current recon drone values.

Open, with the test that would settle each:

- Use and units: look at a stationary enemy from 90 m and 110 m while zoomed and note whether a marker appears (stored 100) and after how long (stored 0.5); then break line of sight and time the marker (stored 5, vehicles 30, gadgets 20).
- Which trait or field upgrade applies the `AdvancedSpot`, `Tracker`, `Bloodhound`, `Ripple`, `Ruthless` and `Despicable` rows: no stored link was traced.
- Seven `Q...Spot_Duration` rows store no readable default and are not recorded.

## L3311 - Soldier rule values in the soldier registry (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3311-soldier-rules.json). Dataset: `reference-data/frosty/registry-soldier-rules.json` (171 rows, each default read back at its raw offset). Registry defaults from `GRX_Glacier_Soldier`, leaving out the spotting rows of L3309 and screen-effect rows. Meaning is read from row names; units and use in a match are unconfirmed. Earlier sections already record the revive, regeneration and sprint rows; they are repeated here only as part of the full list.

| Row | Default | Min | Max |
|---|---|---|---|
| `SuppressionResistance` | 0.75 | 0 | 1 |
| `InfantrySupportSuppressionResistance` | 0.75 | 0 | 1 |
| `InfantrySupportRadius` | 10 | 5 | 15 |
| `KillshotSuppressionResistance` | 0.25 | 0.1 | 0.5 |
| `UnbreakableSuppressionResistance` | 0.25 | 0 | 1 |
| `SuppressionMasteryReduction` | 0.75 | 0 | 1 |
| `ReviveTotalTime` | 4.72 | 0 | 8 |
| `Support_ReviveTotalTime` | 2.2 | 0 | 8 |
| `MedicalTriageTimeReduction` | 0.5 | 0 | 0 |
| `MedicalTriageDefibReduction` | 0.5 | 0 | 1 |
| `ActiveReviveTimeReduction` | 0.7 | 0.5 | 1.5 |
| `ResilientDownedDurationMultiplier` | 0.5 | 0 | 1 |
| `RegenerationDelay` | 5 | 0 | 30 |
| `RegenerationRate` | 10 | 0 | 1000 |
| `DefaultStandSprintTopSpeedMultiplier` | 1.857 | 1 | 3 |
| `FastSprintTopSpeedMultiplier` | 2.05 | 1 | 3 |
| `Slide.CooldownDuration` | 1 | 0 | 10 |
| `CombatDive.CooldownDuration` | 2.5 | 0 | 10 |
| `DraggingSpeedModifier` | 1.2 | 0 | 5 |
| `Mortar_VolleyCount` | 2 | 1 | 32 |
| `Mortar_ShellCountPerVolley` | 2 | 1 | 32 |
| `Mortar_TimeBetweenShells` | 1 | 0 | 60 |
| `Mortar_TimeBetweenVolleys` | 4 | 0 | 60 |
| `Mortar_FireDelay` | 3 | 0 | 60 |
| `Mortar_DispersionRadius` | 8 | 0 | 200 |
| `ArtilleryMasteryMortarReload` | 0.75 | 0.5 | 0.9 |
| `SupplyCratePlusMortarReload` | 0.835 | 0.5 | 0.9 |
| `Artillery_IncreaseShellCountPerVolley` | 1.25 | 1 | 5 |
| `PointmanBase_RespawnMags` | 3 | 0 | 20 |
| `ImproviserRadius` | 25 | 5 | 75 |
| `ImproviserSprintIncrease` | 1.1 | 1 | 1.2 |
| `SERETrainingSprintIncrease` | 1.1 | 1 | 1.2 |
| `ConcealedRescueCooldown` | 40 | 0 | 60 |
| `ScapegoatCooldown` | 30 | 0 | 60 |
| `ScapegoatHealthThreshold` | 45 | 0 | 100 |
| `Provider_MP_LowAmmo_Primary` | 0.25 | 0.001 | 1 |
| `AmmoPassiveRequestLimit` | 0.5 | 0 | 0 |
| `HealingPassiveRequestLimit` | 70 | 0 | 0 |
| `Melee MaxDistance` | 2.5 | 0 | 3 |
| `Zipline_TravelSpeed` | 6.5 | 1 | 10 |
| `Swimming_SwimVelocity` | 3.33 | 0 | 5 |
| `Swimming_SwimSprintVelocity` | 7.65 | 0 | 10 |

Class and kit links: many rows are named after traits or field upgrades (Suppression Mastery, Medical Triage, Artillery Mastery, Improviser, SERE Training, Concealed Rescue, Scapegoat, Pointman). The name is the only link. No stored pointer from a class, kit, trait or upgrade asset to a row was found: no saved file contains the kit node identifiers of the `Category_Kits` tree, the catalog has no trait or signature asset under a kit or class path, and the `KitLimitationGroup` files hold spawner groups only. This search is recorded as a dead end.

Open, with the test that would settle each:

- Which trait or upgrade reads each row: time a revive with and without Medical Triage (stored reduction 0.5 on a Support base of 2.2).
- Suppression resistance meaning (share removed or share kept): record sway or regeneration delay under fire with and without the upgrade whose row stores 0.75.
- Mortar pattern: fire once, count shells and volleys and time the gaps (stored 2 volleys of 2 shells, 1.0 and 4.0).
- Sprint multipliers: time a 50 m sprint with default and fast sprint (stored 1.857 and 2.05; no base speed is stored beside them).

## L3315 - Flak and damage-resistance effects (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3315-resistance-heal-ammo-effects.json). Dataset: `reference-data/frosty/effect-resistance-heal-ammo.json`. Every saved object of the damage-resistance effect class (`Class_7d3d8a5c`, seven objects) was read, each scalar checked at its raw offset. This extends the earlier note that Flak and Stance Flak store 0.67 and 0.75 in an unnamed field.

| Effect file | Multiplier `Field_658381bd` | Explosive flag `Field_0a5e9034` | Bullet flag `Field_ac6090d6` |
|---|---|---|---|
| `Affector_Flak` | 0.67 | true | false |
| `Affector_StanceFlak` | 0.75 | true | false |
| `Affector_Flak_AdrenalineShot` | 0.8 | true | false |
| `Affector_EODBot_ExplosivesResistance` | 0.6 | true | false |
| `Affector_EODBot_BulletResistance` | 0.65 | false | true |
| `Affector_Vehicle_Abilities_MBT_Durability_DamageResistance` | registry row `Passives_Vehicles_MBT_Durability_DamageRecievedMultiplier` (0.85) | true | true |
| `Affector_Vehicle_Abilities_IFV_Durability_DamageResistance` | registry row `Passives_Vehicles_IFV_Durability_DamageRecievedMultiplier` (0.85) | true | true |

How the names were reached:

- **Multiplier: stored link.** The tank and IFV durability effects hold, in place of the value, an import of the registry row named `DamageRecievedMultiplier`. That names `Field_658381bd` as a damage received multiplier. On that reading Flak takes 33% off, Stance Flak 25% and the adrenaline shot 20% (inference).
- **Flags: name only.** The two EOD bot files are named for bullets and explosives and differ only in which flag is set. On that reading all three flak effects apply to explosive damage and not to bullets.
- A third flag, `Field_2c65377f`, imports the registry row `Passives_Vehicles_Shared_Durability_ReduceRepairRate` in the vehicle effects and is false elsewhere.

These effects also show an asset reading the registry directly: the value slot holds a pointer to the registry row, with a fallback number beside it. For such fields the registry row is the stored source (see L3314 in `docs/working/ROSTER_VALUES.md`).

Open, with the test that would settle each:

- Size and stacking: take one frag grenade at a fixed distance with and without the Flak upgrade (stored 0.67), then crouched or prone for Stance Flak (0.75), then after an adrenaline shot (0.8), then with two at once.
- Scope: repeat with a tank high-explosive shell to see whether flak covers vehicle explosives.
- Which soldier state or upgrade turns each effect on was not traced.

## L3329 - Explosive damage to soldiers from the material grid and the flak multipliers (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3329-explosive-soldier-damage.json). Dataset: `reference-data/frosty/explosive-soldier-damage.json`. This applies the vehicle damage rule of L3323 (`docs/frosty/VEHICLES.md`) to soldier targets and combines it with the flak multipliers of L3315. It is a prediction from stored values; no in-game reading confirms it.

What is stored:

- Each explosion's material has a grid cell with a damage value against the soldier abdomen material (25) only. Against the head (24) and limb (26) materials the cell holds no damage record. So a blast is taken to use one value for the whole soldier (inference).
- The projectile materials of shells, rockets and missiles read 1 against head, abdomen and limb, so a direct hit is taken to deal the stored direct damage (the anti-air missiles read 0 against head and limb).
- Values are equal in the Abbasid and Badlands grids.

Full blast is blast damage times the grid value, as inside the inner radius. The flak columns multiply by the stored L3315 values; that the game multiplies them this way is an inference.

| Item | Blast damage | Blast material | Grid value, abdomen (25) | Full blast on a soldier | With Flak (0.67) | With Stance Flak (0.75) | After adrenaline shot (0.8) | Inner / outer radius (registry) |
|---|---|---|---|---|---|---|---|---|
| 120mm HEMP-T Rounds | 100 (registry) | 130 | 1 | 100 | 67 | 75 | 80 | 2.25 / 5 m |
| 120mm HEAT-MP-T Rounds | 100 (registry) | 130 | 1 | 100 | 67 | 75 | 80 | 1 / 5 m |
| MBT Aim-Guided Shell | 200 (registry) | 130 | 1 | 200 | 134 | 150 | 160 | 1 / 3 m |
| IFV HEI-T Rounds | 50 (registry) | 129 | 1 | 50 | 33.5 | 37.5 | 40 | 1 / 4.25 m |
| IFV MPLD round (no EA figure) | 30 (own) | 129 | 1 | 30 | 20.1 | 22.5 | 24 | not stored in the registry |
| IFV Light Rockets | 100 (registry) | 130 | 1 | 100 | 67 | 75 | 80 | 1 / 4 m |
| IFV Aim-Guided Missile | 100 (registry) | 130 | 1 | 100 | 67 | 75 | 80 | 1.75 / 4 m |
| IFV Lock-Guided Missile | 150 (registry) | 650 | 0.85 | 127.5 | 85.425 | 95.625 | 102 | 1 / 5 m |
| Helicopter Light Rockets | 90 (registry) | 591 | 1 | 90 | 60.3 | 67.5 | 72 | 1 / 4.75 m |
| Helicopter Aim-Guided Rockets | 80 (registry) | 591 | 1 | 80 | 53.6 | 60 | 64 | 1 / 4.75 m |
| Attack Helicopter Heavy Rocket | 100 (registry) | 591 | 1 | 100 | 67 | 75 | 80 | 1 / 5.25 m |
| Air-to-Ground Missiles | 150 (registry) | 650 | 0.85 | 127.5 | 85.425 | 95.625 | 102 | 2 / 6.7 m |
| AGM-65 missile (no EA figure) | 150 (registry) | 650 | 0.85 | 127.5 | 85.425 | 95.625 | 102 | 2 / 6.7 m |
| GBU-39 bomb (file name) | 240 (registry) | 213 | 0.8 | 192 | 128.64 | 144 | 153.6 | 2 / 7 m |
| Mk82 bomb (file name) | 335 (registry) | 607 | 0.8 | 268 | 179.56 | 201 | 214.4 | 5 / 10 m |
| MAS 148 Glaive | 155 (registry) | 650 | 0.85 | 131.75 | 88.2725 | 98.8125 | 105.4 | 1 / 4 m |
| RPG-7V2 | 70 (registry) | 164 | 1 | 70 | 46.9 | 52.5 | 56 | 2 / 6 m |
| M136 AT | 70 (own) | 655 | 1 | 70 | 46.9 | 52.5 | 56 | not stored in the registry |
| MBT-LAW | 80 (own) | 650 | 0.85 | 68 | 45.56 | 51 | 54.4 | not stored in the registry |
| 9K93 IGLA | 100 (own) | 185 | 0.6 | 60 | 40.2 | 45 | 48 | not stored in the registry |
| SLM-93A | 100 (own) | 185 | 0.6 | 60 | 40.2 | 45 | 48 | not stored in the registry |
| C-4 | 100 (own) | 95 | 1 | 100 | 67 | 75 | 80 | not stored in the registry |
| M4A1 SLAM (body) | 100 (own) | 91 | 0.4 | 40 | 26.8 | 30 | 32 | not stored in the registry |
| M15 AV Mine | 195 (registry) | 96 | 1 | 195 | 130.65 | 146.25 | 156 | 1.99 / 2 m |
| EOD Bot mine | 150 (own) | 96 | 1 | 150 | 100.5 | 112.5 | 120 | not stored in the registry |
| PTKM-1R | 160 (own) | 650 | 0.85 | 136 | 91.12 | 102 | 108.8 | not stored in the registry |

A full-health soldier (100) at the centre of the blast is killed where the figure is 100 or more. On these numbers Flak (0.67) turns a tank shell, C-4, a light rocket or a heavy rocket from lethal to survivable; the guided shell, the bombs, the M15 and the EOD Bot mine stay lethal.

Compared with EA's statements about soldiers:

- Fits: EA's 1.3.1.0 notes say the tank's aim-guided shell remains lethal within 2 m. Blast damage 200 x 1, falling in a straight line from the inner radius 1 m to the radius 3 m, is exactly 100 at 2 m. The straight-line falloff is an assumption.
- Fits: the notes give land vehicle explosives a minimum explosive damage of 20%; the registry stores `MinimumBlastDamage` 20 for tank HE and HEAT-MP-T (blast damage 100).
- Does not fit: the 1.3.3.0 notes give HEAT-MP-T a total radius of 5 m and a lethal radius of 1.25 m. The registry stores `BlastRadius` 5 and `InnerBlastRadius` 1, and 100 x 1 is lethal only inside the inner radius.

Still open, with the test that would settle each:

- The operation. Stand 1 m from a C-4 pack at full health with no flak: death (100) expected; repeat with the Flak upgrade: 67 expected.
- Stacking. The same with Flak while prone (0.67 and 0.75 together): 50.25 if multiplied.
- Grid values below 1. One MBT-LAW impact at a teammate's feet in a private match: 68 expected (80 x 0.85).
- Falloff shape. A tank HE shell at 3 m and at 4 m from a soldier: a straight line from 100 at 2.25 m to 20 at 5 m gives about 78 and 49.
- HEAT-MP-T lethal radius. The same shell at 1.1 m: death means the lethal radius is wider than the stored inner radius 1.

## L3350 - Soldier registry rows not recorded before (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3350-soldier-registry-global-rows.json). Dataset: `reference-data/frosty/soldier-registry-global-rows.json`. `GRX_Glacier_Soldier` has 238 rows without an owner prefix; 163 of them were not named anywhere in the docs. All are in the dataset with default, minimum and maximum. These are registry defaults: the row name is the only description, units are implied by the name, and nothing here shows which mode reads a row.

Rows matching `Revive / Melee / ThermalSignature / Spot / Mortar / Zipline / FallDamage / Regeneration / Health` (51 of 163):

| Row | Default | Min | Max |
|---|---|---|---|
| `AssaultEngineerRecon_CanReviveTeam` | False | none | none |
| `DraggingReviveTimeMovingModifier` | 1 | 0 | 1 |
| `FallDamage Buffer Delay` | 0.4 | 0 | 3 |
| `Gauntlet_AssaultReconEngineer_ReviveHealthRank` | 6 | 0 | 10 |
| `Gauntlet_Support_ReviveHealthRank` | 6 | 0 | 10 |
| `Granite_AssaultReconEngineer_ReviveHealthRank` | 6 | 0 | 10 |
| `Granite_DraggingReviveTimeMovingModifier` | 1 | 0 | 1 |
| `Granite_ReviveHealthRank` | 6 | 0 | 10 |
| `Granite_ReviveTotalTime` | 4.72 | 0 | 8 |
| `Granite_Support_ReviveHealthRank` | 6 | 0 | 10 |
| `Granite_Support_ReviveTotalTime` | 2.2 | 0 | 8 |
| `ManDownSpottingAllowed` | True | none | none |
| `Melee Attack Angle` | 25 | 0 | 60 |
| `Melee bash align distance` | 1.5 | 0 | 3 |
| `Melee MinDistance` | -0.1 | -1 | -0.1 |
| `Melee takedown Offset - NORMAL` | -15 | -60 | 90 |
| `Melee takedown Offset - Sniper/shotgun` | -28 | -60 | 90 |
| `Melee_NoTarget_Bullet_Distance` | 0 | 0 | 10 |
| `MeleeSecondChance_Angle` | 25 | 0 | 30 |
| `MeleeSecondChance_MaxDistance` | 2 | 0 | 3 |
| `MeleeSecondChance_MaxDistance_InAir` | 2 | 0 | 3 |
| `Mortar_RangeingShotCount` | 0 | 0 | 32 |
| `Mortar_RangeingShotDelay` | 1.5 | 0 | 60 |
| `Mortar_RangeingTimeBetweenShots` | 1 | 0 | 60 |
| `Mortar_TimeBetweenShellsVariation` | 0.333 | 0 | 60 |
| `MP_AssaultReconEngineer_ReviveHealthRank` | 6 | 0 | 10 |
| `MP_Support_ReviveHealthRank` | 0 | 0 | 10 |
| `PostRevive_RegenerationDuration` | 0 | 0 | 15 |
| `RevivePauseBeforeDecayTime` | 1 | 0 | 0 |
| `ReviveProcessDecayRate` | 1 | 0 | 0 |
| `RippleSpotMinimapEnabled` | True | none | none |
| `RippleSpotOcclusionEnabled` | False | none | none |
| `RippleSpotWorldEnabled` | False | none | none |
| `Soldier_InWorld_Enemy_LocalSpottingRadius` | 10 | 0 | 0 |
| `SpotOverlayWhileSwimming` | True | none | none |
| `Swimming_AllowDragAndReviveUnderWater` | True | none | none |
| `ThermalSignature_Crouched_Min` | 0.25 | 0 | 1 |
| `ThermalSignature_InPsyGas` | 0.025 | 0 | 1 |
| `ThermalSignature_InWater_Max` | 0.6 | 0 | 1 |
| `ThermalSignature_InWater_Min` | 0.1 | 0 | 1 |
| `ThermalSignature_Mandown_Max` | 0.1 | 0 | 1 |
| `ThermalSignature_Prone_Min` | 0.1 | 0 | 1 |
| `ThermalSignature_Underwater_Max` | 0.4 | 0 | 1 |
| `Triage_ReviveHealthRank` | 0 | 0 | 10 |
| `Zipline_CharacterTraitSpeedScaleOnRope` | 1.25 | 1 | 2 |
| `Zipline_FastTravelSpeed` | 12.5 | 1 | 20 |
| `Zipline_LauncherMovementGain` | 10 | 1 | 20 |
| `Zipline_LauncherTravelSpeed` | 15 | 1 | 20 |
| `Zipline_LauncherVerticalLift` | 25 | 1 | 60 |
| `Zipline_MinimumAttachTime` | 0.5 | 0 | 3 |
| `Zipline_MovementGain` | 3 | 1 | 15 |

152 raw-offset checks matched.

## L3370 - Soldier materials 579 and 587: the 'against armor' values (9 October 2026)

> Replaced by L3380 below. The statement here that no saved file names these materials came from an incomplete file search; the armor affectors name them.

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3370-soldier-armor-materials-579-587.json). Dataset: `reference-data/frosty/soldier-armor-materials.json`. EA's [1.3.3.0 notes](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-3-0) give a chest multiplier 'against armor' of 0.84 (automatic), 0.91 (DMR) and 0.67 (sniper). L3362 could not place them: the chest material 115 reads 1.0.

`Common/Gameplay/Soldier/Glacier_Soldier` object 55 (`Class_041026f6`) holds two packed materials, 579 and 587, and no other saved file names either. Material 579, both level grids:

| Array value | Scalar | Projectile materials |
|---|---|---|
| 0.67 | 0.67 | 290, 351 |
| 0.84 | 0.7353 | 621 |
| 0.84 | 0.84 | 276, 277, 278, 492, 493, 494, 496, 497, 288, 289 |
| 0.91 | 0.91 | 291, 498 |
| 1 | 1 | 275, 279, 286, 491, 499, 784 |

- 579 is the only target material with the 0.84 / 0.91 / 0.67 set; here the scalar equals the array.
- 587 is a head table equal to the normal one except for bolt-action bullets (290, 351, 784): `[1, 2.25, 2.25, 2.25, 3]`, so 2.25 at the bolt-action index 3 instead of 1.75.
- That 579 is the armored chest is a correspondence with EA's lines; the fields naming it are hashes and what selects it is not read.

64 raw-offset checks matched.

Test: in a mode with armor plates, one rifle bullet to the chest of a plated and of an unplated enemy at the same range.

## L3374 - Dead end: 13 unidentified target materials with soldier-style arrays (9 October 2026)

> Replaced by L3380 below. The statement here that no saved file names these materials came from an incomplete file search; the armor affectors name them.

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3374-unidentified-soldier-style-target-materials.json). Dataset: `reference-data/frosty/unidentified-target-materials.json`. Beyond the player soldier's materials (24, 115, 25, 26; and 579, 587 of L3370), these target materials have a multiplier array against bullets. Single values, or for tables the entries at index 1 / 2 / 3 / 11:

| Target material | automatic (276) | DMR (498) | bolt-action (290) | pistol (275) | shotgun (279) |
|---|---|---|---|---|---|
| 74 | 1 | 1 | 0.67 | 1 | 1 |
| 238 | 3 | 3.8 | 4 | 2.51 | 1.475 |
| 239 | 0.48 | 0.475 | 0.5 | 0.43 | 0.48 |
| 292 | table: 0.648 / 0.816 / 0.816 | table: 0.64125 / 0.8075 / 0.9975 | table: 0.675 / 0.85 / 1.05 | table: 0.5805 / 0.731 / 0.903 | table: 0.48 / 0.48 / 0.48 |
| 394 | 0.74 | 0.85 | 0.583 | 0.74 | 0.48 |
| 395 | table: 0.999 / 1.258 / 1.554 | table: 1.475 / 1.445 / 1.785 | table: 0.78705 / 0.9911 / 1.2243 | table: 0.999 / 1.258 / 1.554 | table: 0.48 / 0.48 / 0.48 |
| 418 | 1 | 1 | 0.5 | 1 | 1 |
| 419 | 1 | 1 | 0.583 | 1 | 1 |
| 420 | 1 | 1 | 0.5 | 1 | 1 |
| 421 | 1 | 1 | 0.583 | 1 | 1 |
| 535 | table: 1.34 / 1.5 / 1.75 / 1.4 | table: 3 / 3.777 / 4.666 | table: 2.777 / 3.333 / 3.333 | table: 1.34 / 1.5 / 1.75 / 1.4 | table: 1.34 / 1.5 / 1.75 / 1.4 |
| 536 | 0.84 | 2.2223 | 2.223 | 1 | 1 |
| 586 | table: 1.34 / 1.5 / 1.75 / 1.4 | table: 1.34 / 1.5 / 1.75 / 1.4 | table: 1.34 / 1.5 / 1.75 / 1.4 | table: 1.34 / 1.5 / 1.75 / 1.4 | table: 1.34 / 1.5 / 1.75 / 1.4 |

No saved file names any of them (47,686 files searched) and the bone collision file uses only 24, 115, 25 and 26. What they belong to is not readable from the capture. 89 raw-offset checks matched.

## L3380 - Armor is stored as material swaps (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3380-armor-upgrade-material-swaps.json). Dataset: `reference-data/frosty/armor-material-swaps.json`. Replaces L3370 and withdraws L3374 above: their file search was incomplete (three raw roots, low bits required to equal 0x80). Armor affectors do name these materials.

Swap affectors (`Class_99b2c2df`; kind 1 soft, 2 ceramic):

| Affector file | Kind | Pairs (first to second) |
|---|---|---|
| `Affector_CeramicArmorUpgrade` | 2 | 579 to 238, 580 to 239, 580 to 292, 0 to 239, 0 to 239 |
| `Affector_CeramicArmorUpgrade_EffectiveHealth` | 2 | 587 to 586, 579 to 579, 580 to 580, 581 to 581, 580 to 580, 580 to 580 |
| `Affector_CeramicArmorUpgrade_ExtraDurability` | 2 | 397 to 445, 395 to 450, 396 to 449, 395 to 450, 395 to 450 |
| `Affector_CeramicArmorUpgrade_ExtraProtection` | 2 | 397 to 447, 395 to 451, 396 to 489, 395 to 451, 395 to 451 |
| `Affector_FiringRange_TargetCeramicArmor` | 2 | 0 to 3, 394 to 3, 395 to 3, 421 to 3, 419 to 3 |
| `Affector_FiringRange_TargetSoftArmor` | 1 | 0 to 3, 394 to 3, 395 to 3, 421 to 3, 419 to 3 |
| `Affector_SoftArmorUpgrade` | 1 | 579 to 579 |
| `Affector_SoftArmorUpgrade_EffectiveHealth` | 1 | 587 to 587, 579 to 579, 580 to 580, 581 to 581, 580 to 580, 580 to 580 |
| `Affector_SoftArmorUpgrade_ExtraDurability` | 1 | 397 to 446, 395 to 452, 396 to 454, 395 to 452, 395 to 452 |
| `Affector_SoftArmorUpgrade_ExtraProtection` | 1 | 397 to 448, 395 to 453, 396 to 488, 395 to 453, 395 to 453 |

Grid values of the materials named, single value or table entries 1 / 2 / 3 / 11:

| Target material | automatic (276) | DMR (498) | bolt-action (290) | pistol (275) | shotgun (279) |
|---|---|---|---|---|---|
| 3 | no array, scalar - | no array, scalar - | no array, scalar - | no array, scalar - | no array, scalar - |
| 238 | 3 | 3.8 | 4 | 2.51 | 1.475 |
| 239 | 0.48 | 0.475 | 0.5 | 0.43 | 0.48 |
| 292 | table 0.648/0.816/0.816 | table 0.6412/0.8075/0.9975 | table 0.675/0.85/1.05 | table 0.5805/0.731/0.903 | table 0.48/0.48/0.48 |
| 394 | 0.74 | 0.85 | 0.583 | 0.74 | 0.48 |
| 395 | table 0.999/1.258/1.554 | table 1.475/1.445/1.785 | table 0.7871/0.9911/1.2243 | table 0.999/1.258/1.554 | table 0.48/0.48/0.48 |
| 396 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 397 | no array, scalar - | no array, scalar - | no array, scalar - | no array, scalar - | no array, scalar - |
| 419 | 1 | 1 | 0.583 | 1 | 1 |
| 421 | 1 | 1 | 0.583 | 1 | 1 |
| 445 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 446 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 447 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 448 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 449 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 450 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 451 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 452 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 453 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 454 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 488 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 489 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 | no array, scalar 1 |
| 579 | 0.84 | 0.91 | 0.67 | 1 | 1 |
| 580 | 0 | 0 | 0 | 0 | 0 |
| 581 | table 0/0/0 | table 0/0/0 | table 0/0/0 | table 0/0/0 | table 0/0/0 |
| 586 | table 1.34/1.5/1.75/1.4 | table 1.34/1.5/1.75/1.4 | table 1.34/1.5/1.75/1.4 | table 1.34/1.5/1.75/1.4 | table 1.34/1.5/1.75/1.4 |
| 587 | table 1.34/1.5/1.75/1.4 | table 1.34/1.5/1.75/1.4 | table 2.25/2.25/2.25 | table 1.34/1.5/1.75/1.4 | table 1.34/1.5/1.75/1.4 |

Amount affectors (`Class_79520af1`):

| Affector file | Entries: integer / amount / factor |
|---|---|
| `Affector_Gadget_CeramicArmor` | 1 / 121 / 0.5, 1 / 242 / 0.5, 2 / 40 / 0.5, 2 / 80 / 0.5, 1 / 40 / 0.5, 1 / 80 / 0.5 |
| `Affector_Gadget_CeramicArmor_Full` | 1 / 80 / 0.5, 1 / 80 / 0.5, 1 / 80 / 0.5 |
| `Affector_Gadget_SoldierArmorVestTier` | 1 / 0 / 0.5, 1 / 40 / 0.5, 2 / 0 / 0.5, 2 / 40 / 0.5, 2 / 80 / 0.5, 1 / 0 / 0.5, 1 / 40 / 0.5, 1 / 80 / 0.5 |
| `Affector_Gadget_SoftArmor` | 1 / 242 / 0.5, 1 / 242 / 0.5, -1 / 242 / 0.5, 1 / 40 / 0.5, -1 / 242 / 0.5 |

- Soldier file: chest candidate 579 (EA's [1.3.3.0](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-game-update-1-3-3-0) 'against armor' 0.84 / 0.91 / 0.67), head candidate 587 (bolt-action 2.25).
- Ceramic armor maps 579 to 238 and 587 to 586 (bolt-action head 1.75). Soft armor keeps both.
- The direction of a pair (first replaced by second) and the meaning of 40 / 80 / 121 / 242 are candidates; field names are hashes.
- Still without a user: 74, 418, 420, 535, 536.

202 raw-offset checks matched.

Test: one rifle bullet to the chest of an armored enemy, reading health and armor lost; one bolt-action headshot on an armored enemy.

## L3381 - Damage affectors: field names and stored values (9 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-09-L3381-damage-affector-fields-and-values.json). Dataset: `reference-data/frosty/damage-affectors.json`. Class `Class_14965f9f` (the fire affectors of L3379 in GADGETS.md use it too). Registry rows named after the defibrillator affector and the Thermal Smoke infantry damage name three fields: `Field_72380a66` InitialDamage, `Field_ce8df685` DamageInterval, `Field_093fdee2` DamageToDealPerSecond.

| Affector file | Entry | InitialDamage | DamageInterval | DamageToDealPerSecond | Material | Stages (integer / float) |
|---|---|---|---|---|---|---|
| `Affector_Melee_Damage` | 0 | 35 | 0.5 | 0 | 274 | - |
| `Affector_Melee_Damage` | 1 | 60 | 0.5 | 0 | 274 | - |
| `Affector_Melee_Damage` | 2 | 1500 | 0.1 | 0 | 274 | - |
| `Affector_Melee_Damage` | 3 | 70 | 0.5 | 0 | 274 | - |
| `Affector_Damage_Defibrillator` | 0 | 50 | 0 | 0 | 100 | - |
| `Affector_Damage_Defibrillator` | 1 | 60 | 0 | 0 | 100 | - |
| `Affector_Damage_Defibrillator` | 2 | 70 | 0 | 0 | 100 | - |
| `Affector_Damage_Defibrillator` | 3 | 80 | 0 | 0 | 100 | - |
| `Affector_Damage_Defibrillator` | 4 | 90 | 0 | 0 | 100 | - |
| `Affector_Damage_Defibrillator` | 5 | 100 | 0 | 0 | 100 | - |
| `Affector_PsyGas_Damage` | 0 | 0 | 0.5 | 24 | 169 | - |
| `Affector_ThermalSmoke_InfantryDamage` | 0 | 12 | 0.5 | 12 | 169 | - |
| `Affector_ThermalSmoke_InfantryDamage` | 1 | 25 | 0.25 | 12 | - | - |
| `Affector_VelocityDamage` | 0 | 0 | 0 | 0 | - | - |
| `Affector_VelocityDamage` | 1 | 25 | 0 | 0 | - | - |
| `Affector_VelocityDamage` | 2 | 50 | 0.5 | 0 | - | - |
| `Affector_VelocityDamage` | 3 | 75 | 0.5 | 0 | - | - |
| `Affector_VelocityDamage` | 4 | 100 | 0.5 | 0 | - | - |
| `Affector_VelocityDamage` | 5 | 999 | 0.5 | 100 | - | - |
| `Affector_Damage_M26Dragonbreath` | 0 | 0 | 0.1 | 1 | 169 | 3 / 5, 2 / 2, 4 / 1 |
| `Affector_Damage_M26Dragonbreath` | 1 | 0 | 0.1 | 1 | 169 | 3 / 2, 2 / 1 |
| `Affector_Damage_Afterburner` | 0 | 0 | 0.1 | 1 | 169 | 8 / 5, 7 / 6.5, 5 / 7 |

- Melee: 35 / 60 / 70 and a 1500 takedown; which swing uses which is not read.
- Defibrillator: 50 to 100 in six steps (the registry holds the same rows).
- Gas: 24 per second at a 0.5 interval. Thermal Smoke against infantry: registry 25 initial, 12 per second, 0.5 interval.
- Collision: steps 0, 25, 50, 75, 100, 999; thresholds not in this file.
- Stage lists (Dragon's Breath, afterburner, fire) remain unnamed.

75 raw-offset checks matched.

Tests: one knife swing front and back; defibrillator on an enemy uncharged and charged; health lost per second in gas.

## L4013 - Melee loadout values and sprint speed (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4013-melee-loadout-values-and-sprint-state.json). Loadout screen (operator): knives, Ice Axe, Serrated Blade, EOD Bot Arm and Diver's Knife show Hit Delay 100 ms, Damage 35; Sledgehammer 200 ms, 60.

- Damage: `Affector_Melee_Damage` entry 0 is 35 and entry 1 is 60, so entry 1 is the Sledgehammer. Entry 2 (1500) is the takedown; entry 3 (70) is unassigned.
- Hit delay: one unnamed block in the three melee firing files, slot D, reads 0.1 (knives) and 0.2 (Sledgehammer). The EOD arm reads 0.15 there against a displayed 100 ms.

| Firing file | A | B | C | D |
|---|---|---|---|---|
| `Melee_Shared_WeaponFiring` | 0.1 | 0.1 | 0 | 0.1 |
| `Melee_Shared_Sledgehammer_WeaponFiring` | 0 | -1 | 0.1 | 0.2 |
| `Melee_Shared_EODArm_WeaponFiring` | 0.1 | 0.1 | 0.05 | 0.15 |

- Sprint speed: no stored bonus for knife, defibrillator or repair tool. `MSA_Hip_Melee` and `MSA_Hip_Weapons` are both [1]; all 36 gadget blueprints use sprint settings index 0 and those files hold recovery times only; the only sprint multipliers are the soldier rows 1.857 and 2.05. An unowned gadget registry row `SprintModifier` 2.0 has no identified consumer.

Test: time a fixed sprint distance holding a rifle, a knife, the defibrillator and the repair tool.

24 raw-offset checks matched.

## L4014 - Sprint speed: stored speeds and the fast-sprint flag (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4014-sprint-speed-stored-values-and-fast-sprint-flag.json). - `FastSprintRequired` (soldier public channel) is referenced once each by the abilities of Combat Knife, Geko Knife, Dino Machete, Ice Climbing Axe, EOD Arm, Dive Knife (1.4.3.0), the defibrillator and the repair tool. The Sledgehammer ability, the adrenaline shot and all weapon blueprints do not reference it.
- `Glacier_Soldier` pose entries (`Class_7845fbab`) store two speeds, `Field_1a2b6380` and `Field_e4506828`:

| Pose identifier | First speed | Second speed | Note |
|---|---|---|---|
| 475999738 | 3.5 | 6.05 | standing (0.6 x 1.0 x 1.2 size entry) |
| -872007306 | 2.1 | 4.7 | crouch-sized |
| 963439859 / 963439860 | 3 | 5.285 | narrow standing |
| 475102768 | 0.9 | 0.9 | prone-sized |
| 963439863 | 1.2 | 1.2 |  |
| 963439862 | 0.9 | 0.9 |  |
| 963439857 | 7.15 | 7.15 | low and long (1.25 x 0.25 x 1.3) |

Published measurements (TheXclusiveAce, November 2025 and July 2026) against stored values:

| In hand | Measured (m/s) | Stored match |
|---|---|---|
| Walking, any item | 3.5 | standing pose first speed 3.5 |
| Gun except LMG, sprint | 6.05 | standing pose second speed 6.05 |
| LMG without Support proficiency | 5.75 | 0.95 x 6.05; no stored 0.95 found |
| Gun with adrenaline shot | about 6.65 | 1.1 x 6.05 = 6.655; two soldier rows read 1.1 |
| Sledgehammer (July 2026) | 6.5 | 1.857 x 3.5 = 6.4995 |
| Knife-type melee, defibrillator, repair tool | 7.15 | 2.05 x 3.5 = 7.175, or 1.1 x 6.5 = 7.15; a pose entry also stores 7.15 |

- The size of the fast sprint is matched by value only; the equation is not read. This supersedes the L4013 line that no stored value relates to the bonus.
- July 2026 timings before the EOD Bot Arm change (1.4.2.5): EOD arm 400 ms to first hit and 800 ms between hits, Sledgehammer 1100 ms between hits; the speaker says menu hit-delay values do not match in-game timing.

Test: timed sprint with a rifle, an LMG, a knife and the Sledgehammer.

16 raw-offset checks matched.

## L4015 - Movement-speed logic: inputs and constants (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4015-move-speed-modifier-inputs-and-constants.json). Chain: item ability sets `FastSprintRequired` -> `SoldierMotionMachine` parameter -> `SimEx_RootLayerLogic` input 79 -> compiled resource `2bfca9f18b8f10e9`, parts `SimEx_MoveSpeedModifiers` and `SimEx_Sprinting_States`.

Inputs of the movement-speed block:

| Input | Name | Kind |
|---|---|---|
| 70 | `SprintStrafeAllowed_PerTeam` | mutator |
| 71 | `SoldierMovementSpeedMultiplier_PerTeam` | mutator |
| 72 | `AI_SoldierMovementSpeedMultiplier_PerTeam` | mutator |
| 73 | `DraggingSpeedModifier` | soldier registry |
| 75 | `LMG` | categorization tag |
| 76 | `MachineGun` | categorization tag |
| 77 | `CurrentStance` | soldier channel |
| 78 | `ConcussionGrenade_Movement Speed Modifier` | gadget registry |
| 79 | `FastSprintRequired` | soldier channel |
| 80 | `FastSprintTopSpeedMultiplier` | soldier registry, 2.05 |
| 81 | `DefaultStandSprintTopSpeedMultiplier` | soldier registry, 1.857 |
| 84 | `Affector_Suppression_AdrenalineShot` | affector |
| 85 | `Affector_MedicalTriageSprint` | affector |
| 86 | `Affector_EnhancedFiltering` | affector |
| 87 | `Affector_ConcussionGrenade` | affector |
| 88 | `Affector_BarbedWire_SpeedSlowdown` | affector |
| 89 | `Affector_SwiftTriageSprint` | affector |

- Compiled constants at 4628, 4632, 4636: 1.1, 0.95, 1.1818. On the stored sprint speed 6.05 (L4014): 6.655 (adrenaline, measured about 6.65), 5.7475 (LMG, measured 5.75), 7.1499 (knife, defibrillator, repair tool, measured 7.15).
- Not disassembled: the pairing of constant and condition is by value and adjacency. The Sledgehammer's 6.5 and the role of the 2.05 / 1.857 multipliers stay open.

7 raw-offset checks matched.

## L4016 - Movement-speed logic disassembled (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4016-move-speed-modifiers-disassembled.json). Read from the compiled resource `2bfca9f18b8f10e9` (section `SimEx_MoveSpeedModifiers`); variable names come from the `SoldierMotionMachine` parameter lists.

```
StandSprintTopSpeedMultiplier = FastSprintActive ? FastSprintTopSpeedMultiplier (2.05) : DefaultStandSprintTopSpeedMultiplier (1.857)

FastSprintActive = FastSprintRequired AND NOT SP_IsSPMode AND FastSprintAllowed_PerTeam
SprintRecoverTime = SprintRecoverTimeMultiplier * (FastSprintActive ? 1.75 : 1)

if barbed wire affector:            m = 0.25
elif concussion affector:           m = ConcussionGrenade_Movement Speed Modifier
elif IsManDown:                     m = GraniteDownedStimActive ? 1.5 : 1
else:
    w = IsSPAI ? 1 : WeaponMoveSpeedMultiplierInput
    if Sprint:
        boost = (MedicalTriageSprint or AdrenalineShot or EnhancedFiltering or SwiftTriageSprint affector) ? 1.1 : 1
        lmg   = (NOT flagA and (LMG tag or MachineGun tag) and stance check) ? 0.95 : 1
        w     = w * boost * traitsprintspeed * lmg
        cap   = FastSprintRequired ? 1 : 1.1818
    else:
        cap   = 1
    m = clamp(w, 0, cap)
WeaponMoveSpeedMultiplierOutput = m * f(firing ? 0.8 : 1, ...)      (dragging: DraggingSpeedModifier instead)
```

- Knife, defibrillator, repair tool: 3.5 x 2.05 = 7.175 m/s (measured 7.15). Sledgehammer: 3.5 x 1.857 = 6.50 (measured 6.5). The cap of 1.0 under fast sprint is why adrenaline does not stack on a knife.
- 1.1818 is the modifier ceiling without fast sprint, not the knife bonus (corrects L4015). 1.1 is shared by four sprint affectors; 0.95 is the LMG penalty.
- Open: guns measure 6.05, which needs a weapon input of about 0.931 that is not stored in any file searched.
- Format notes, listing and the reader are in the run folder (`move-speed-disassembly`).

30 raw-offset checks matched.

## L4018 - Melee damage entry selection (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4018-melee-graph-damage-entry.json). Read from the compiled `SimEx_Melee` resource `25ca266bea810e41` (1.4.3.0 capture). Entries of `Affector_Melee_Damage` are 35, 60, 1500, 70 (L4013).

```
entry = switch TakedownAttackerMeleeWeaponID: case 2 -> 1, otherwise -> 0          (0x6b14)
if cmp(HallucinationLevel, 2): entry = 3                                           (0x35cc)
apply Affector_Melee_Damage[entry] to the target                                   (0x365c)
single player local player: Affector_Melee_Damage_SP[entry] instead                (0x3444)
takedown victim: Affector_Melee_Damage[2] with parameter 0.2                       (0x4a18)

reach = (2 < f(AimPitch, curve) < 2.55) ? 2.55 : 1.65                              (0x2f0c)
a second test requires -1.41 < AimPitch < -0.649 (radians, looking down)           (0x3044)
```

- Damage is chosen by melee weapon ID, not stored per weapon: ID 2 gives 60 (Sledgehammer by the loadout screen), every other ID 35.
- Entry 3 (70) needs a state test whose variable resolves by index to `HallucinationLevel`; unconfirmed.
- Entry 2 (1500) is the takedown kill.
- No hit-delay constant is in this graph.

19 raw-offset checks matched.

## L4020 - Melee target finding and class trait graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4020-melee-targeting-and-trait-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/melee-traits.md`).

- `SimEx_FindTargets` / `SimEx_FindTargets_QuickFind`: target finding runs only for `CurrentAction` 0, 3 or 13 (QuickFind also 12 and 1). Speed threshold 2 adds 0.3 to the maximum distance and 5 degrees to the attack angle. Base limits are `GRX_Glacier_Soldier` tunables.
- Takedown: back angle is the `TakeDown BackAngle` tunable, or -115 when a moving flag is set; the relative angle is bucketed at 45 and 135 degrees.
- `SimEx_Melee`: three latches of the form clamp(stored + dt / T, 0, 1) with T = 0.45 (`AffectedByMeleeBlocked`), 0.1 (`BlockMeleeFiring`) and 0.25 s. `Affector_InTakeDown_DamageModifier` is applied with parameter 3.3.
- Active Medic: sphere radius 7, tick period 1, heal and ammo affectors with parameter 1.1, self affector with parameter 10. Active Attack: radius 10, 4.9 s timeout.
- Other traits, the freeze mechanic and the two mutator-copy graphs are tabulated in the findings file; those rows are a delegated reading and are not individually raw-checked.

20 raw-offset checks matched.

## L4022 - Root soldier graph: combat dive, slide and vault start rules (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4022-root-graph-dive-slide-vault.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/root-part-1.md`).

- Combat dive (0x112c8, copy at 0x18c68): gate `CombatDiveAllowed_PerTeam`; speed > 4.0 x `AppliedSPMovementSpeedModifier`; `TimeSinceLastDiveOrSlide` > `CombatDive.CooldownDuration`; `CurrentAction` 0, or 1 within 0.134 s of `LastTimeOnGround`; then `RequestCombatDive = Sprint AND InputProne`. A 0.25 timer condition also applies.
- Slide (0x15c04): gate `SlideAllowed_PerTeam`; speed > `Slide.AccumulatingThreshold.NeededVelocity` x `SoldierMovementSpeedMultiplier` x `AppliedSPMovementSpeedModifier`; a charge divided by `Slide.AccumulatingThreshold.NeededTime` must reach 1.0 unless a slide is already requested or buffered; `TimeSinceLastDiveOrSlide` > `Slide.CooldownDuration`; then `RequestSlide` is set.
- Dive and slide share one timer, `TimeSinceLastDiveOrSlide`, capped at 10 and frozen during actions 13 and 25.
- Vault: input direction thresholds +0.1 and -0.1; minimum obstacle height 0.31 (AI), 0.7 when speed exceeds 4.0, else 0.51; maximum from `Vault_StartHeightMax` or `Vault_StartHeightMaxDirectional`; after a jump the start height adds clamp(current height - `LastJumpHeight`, 0, 1).
- `OptionSprintVaultOver`: vault-over is allowed when the option is off, or when sprinting.

9 raw-offset checks matched.

## L4023 - Man-down bleed-out and revive graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4023-mandown-bleedout-and-revive-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/soldier-state.md`).

- `SimEx_IsInManDown`: `IsBledout` is set when `HealthValue` < -90. Drain = rate x frame time. Rate table 1.6667, 2.2222, 3.3333, 1.1111, selected by `ManDownExperienceType`; a fast case uses 200. Divided by a request-revive slowdown tunable (separate values for multiplayer, battle royale, Gauntlet and single player) and by `HemostaticSmoke_BleedoutMulti`.
- `SimEx_DragRevive_Team`: total time from `ReviveTotalTime`, the Support and battle royale variants and `ActiveReviveTimeReduction`, floored at 0.1. Remaining time counts down by frame time x modifier; the modifier is `DraggingReviveTimeMovingModifier` when the reviver's speed is at least `Deathflow_MovingReviveSpeedThreashold` and the revive is past its first 0.75 s and before its last 0.7 s, otherwise 1.
- Revive completion applies `AffectorRevive_HealthRestored` (entry chosen by a per-class health rank tunable), `AffectorRevive_Regen` (parameter `PostRevive_RegenerationDuration`), conditionally `Affector_Gadget_CeramicArmor` (parameter 0.1, entry 2), and removes the man-down damage modifier.
- Defibrillator revive (`SimEx_GetRevive`) applies `AffectorRevive_Defibrillator_Revive` with parameter 0.5.
- Redeploy and self-kill flags are set in `SimEx_DamageReceived` (L4019). No spawn-protection or friend/foe rule was found in these graphs.

11 raw-offset checks matched.

## L4024 - Traversal graphs: fall bands, slide strength, ground support (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4024-traversal-graphs-fall-slide-support.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/traversal.md`).

- `SimEx_InAirExpressions`: landing class by vertical speed vy: above -6.2 class 0, above -13 class 1, above -15.7 class 2, above -18.45 class 3, above -21.23 class 4, above -29.5 class 5, otherwise 7; class 6 for a jump landing above -13. A second copy fires only when close to ground with vy below -2. No damage is applied in this graph.
- `SimEx_SlidingLogic`: factor = (clamp(`TimeSinceLastDiveOrSlide`, 1.25, 2.5) - 1.25) / 2.5 + 0.5; slide limit = clamp(factor x `Slide.ImpulseLength` x curve(speed) / 6.5, 0, 1); slide speed clamped to 5..100.
- `SimEx_CheckSupport`: OnGround when ground distance < 0.1, CloseToGround when < 0.3, and a next-frame prediction using distance + vy x frame time.
- Swimming vault (`SimEx_CheckStartVault_Swimming`): window from 1.25 up to `Vault_Swimming_StartHeightMax`, with constants 0.5, 0.4 and 0.2.
- In-air vault runs only for non-AI soldiers holding the vault input. Parachute steering is slew-limited at 0.8 per second with drag capped at 50; ladder entry has a 75 degree facing cone; zipline and rope detach on jump, crouch, vehicle entry or abort. These rows are a delegated reading and not individually raw-checked.

16 raw-offset checks matched.

## L4025 - Root soldier graph: stance, prone, swimming bands, parachute, vault window, slide input (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4025-root-graph-stance-parachute-vault-input.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/root-part-3.md`).

- Stance (0xa2c0 to 0xad78): a change between prone and stand or crouch starts a 0..1 timer advancing by frame time / `TransitionInputBlockTime`; `TransitionInputBlock` is true until it completes.
- Prone entry (0xe4a4): requires not `ZipLineAttach`, not `HangingRopeAttached`, and `ProneAllowed_PerTeam` (AI: `AI_ProneAllowed_PerTeam`). Stance values 0, 1, 2 read as stand, crouch, prone.
- Stance override (0xf3a4): `StanceOverride` value 7 means none; otherwise it sets the physics shape.
- Swimming depth bands: thresholds 0.2, 0.6, 1.2 with a 0.2 s hold in the newer classifier; 0.25, 0.8, 1.5 in the legacy one.
- Parachute (0x22964, 0x387a0): `Parachute.InCooldown` until 0.6 s after `Parachute.TimeSinceCut` and only in actions 1, 11, 25, 27; auto-deploy when ground distance is between `Parachute.AutoDeploy.DistanceToGround` - 1.5 (or 5.0 during insertion) and + 1.0; armed by a downward probe of length 0.8 x 150.
- Slide clock (0x2a8a0): `TimeSinceLastDiveOrSlide` counts up to 10 and pauses in actions 13 and 25; slide state gate is action 0, or 1 or 12 outside certain fall-speed bands.
- Vault window (0x3e288): while `InAirFromJump`, maximum height = `Vault_StartHeightMax` (forward or idle) or `Vault_StartHeightMaxDirectional` (other directions) minus clamp(height now - `LastJumpHeight`, -0.25, 0.67); obstacle height bands at 1.9, and 0.9 and 1.4, pick the vault variant; inputs are clamped to +-0.99 with a 0.1 dead zone.
- Slide input (0x3a980): with the slide input held, slide if `TargetStance` is 0 or 1; otherwise `OptionSlideOnCrouchNetworked` chooses crouch toggle, crouch hold, or both. The moving test includes prone speed above 1.5 and excludes steep slopes.
- Prone movement is limited by obstacle and ground probes (three inlined copies); detail in the findings file.

18 raw-offset checks matched.

## L4028 - Player-owner and gameplay feature graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4028-player-and-feature-graphs.json). Read from compiled expression graphs with `exgraph.py`; detail in the run folder (`expression-graphs/findings/player-features.md`).

- Respawn delay (`ActSimEx_PlayerOwner_UpdateOnChange`, 0x0 to 0x8b4): `GameMode_RespawnDelay_Team1/2`, else `DefaultRespawnDelay`, x `Generic_RespawnDelayMultiplier_PerTeam` x `SoldierRespawnDelayMultiplier_PerTeam`; Gauntlet subtracts `Gauntlet_Mission_PlacementRedeployTimeBonus`. In `SimEx_PlayerOwner` the redeploy timer is clamped between `MinRespawnTime` and 150 (a 100 clamp also exists).
- Psy gas (`SimEx_PsyGasLogic`): hallucination amount 0..1 with Mid and Top thresholds, snapped to 0 below 0.0001; health regeneration blocked above `PsyGas_BlockHealthRegenThreshold`; damage over time only at hallucination level 2, with no mask, and health at or above 35. Gas volumes apply `Affector_PsyGas_Damage` with parameter 1.1 once per second.
- Contracts: every contract-values graph is one game-mode switch (2 battle royale, 3 Conquest, 4 Breakthrough, 13 Tactical Obliteration, 10 unnamed) picking a timer and a count tunable; each objective type needs its kill switch off and its mutator on; drop rates come from `BaseDropRate_<mode>`.
- Thermal signature: updated every 0.25 s with 0.25 smoothing and a 0.05 floor; depends on stance, water and speed; a soldier being revived fades toward 0.5.
- Spotting: capture-point self-unspot radius 5; Rush objective 8 m for 30 s; suppression above 0.5 spots the suppressor for 5 s; ping and spot durations come from spot-duration tunables.
- Heat zone: `Affector_Heat_StatusEffect` with parameter 0.5 every `InsideHeatZone_ExecutionInterval`; dynamic gas stops at 95 % progress (these two were checked by the reader against the 1.4.3.0 bodies only).

12 raw-offset checks matched.

## L4034 - Tunable defaults for names read by expression graphs (10 October 2026)

[Receipt](../../reference-data/provenance/frosty-2026-10-10-L4034-tunable-defaults-for-graph-names.json). Joined from the tunable files (`GRX_*`, `MutatorDatabase_*`, kill switch files); table in the run folder (`expression-graphs/tunables-joined.tsv`).

- The table `expression-graphs/tunables-joined.tsv` lists 901 tunables read by simulation graphs: file, name, kind, default, minimum, maximum and the graphs that read each.
- Soldier: stance change input block 0.95 s; vault start height 1.97 forward and 1.4 in other directions (2.4 swimming); parachute auto-deploy distance 13; revive total time 4.72 s; slide cooldown 1.0 s, slide needs speed 5.2 for 0.25 s; melee maximum distance 2.5; active revive time reduction 0.7.
- Gadgets: defibrillator full charge 1.0 s with minimum 0.3 s, friendly range 2.0 and enemy range 1.5; EIDOS alive timer 5 s and 3 intercepts; adrenaline shot 8 s; drone out-of-bounds limit 3 s; improved jammer radius x 2; sabotage distance 2.4; mortar dispersion radius 8.
- Other: passive mastery experience interval 30 s; minimum respawn time 1.5 s; spot duration 8 s; spot-on-fire duration 0.4 s; psy gas blocks health regeneration above 0.15; Phalanx aim rotation speed 270.
- Defibrillator charge time from L4026 therefore defaults to clamp(1.0 - 0.7, 0.3, 1.0) = 0.3 s when the active-revive reduction applies in full (the condition for the reduction is not read).

18 raw-offset checks matched.
