# Soldier mechanics

[Weapons](WEAPONS.md) · [Research queue](../working/FROSTY_RESEARCH_QUEUE.md)

This page records multiplayer soldier source configuration and display proposals. Serialized values, inferred meanings and effective match behavior are separate. Current reads use 1.4.3.5, Head 4909002, descriptor `4c28ad656c175d9a8540245a3e6b57284c2e54d76cbd41b4ab480be1024816a1`. Earlier receipts retain their original build and Head.

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

The [summary receipt](../../reference-data/provenance/frosty-2026-10-01-L844-soldier-field-atlas.json) retains `C:\Users\royal\Documents\BF6 Datamining\reports\weapon-analyzer-research\2026-10-01T001825-0400-soldier-frontier\soldier-atlas.json` with 29 unique inspected owners, 423 owner-family entries and 155 UI records. The mechanic classification covers 34 groups: {'modeled': 8, 'traced not on site': 8, 'known limit': 13, 'never examined': 5}. Family entries can overlap between bounded owner passes. Every inspected family keeps its type identity, fields, observed variants and artifact provenance. This is a bounded field atlas; the multiplayer owner frontier is still open.

The site currently models ADS movement multipliers, sprint recovery, deploy/holster ladders, health-target input, regeneration delay and fire-detection ranges. It does not establish their native composition. Remaining work starts with firing slowdown, stance speeds, ladder transitions, revive/regen consumers, class selection, suppression and mode settings. The current control and parent raw rereads passed.

The official [Season 5 preview](https://www.ea.com/games/battlefield/battlefield-6/news/battlefield-6-community-update-siege-of-vegas-incoming) places training-path revisions and faster armor application in its Battle Royale section. No specific multiplayer soldier numeric change is stated there. Shared Common path/affector assets require a multiplayer recheck after the update; announced BR effects are excluded from current MP proposals.

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
WPM_SupportTrait exactly selects ADS Anim/FOV children with Field_9540bd8e +1 each. This inspected family does not establish a sprint exemption receiver.
WM_WeaponSwap retains selector7727fe65-6ddd-4d10-aeb8-e2d1e59c9054 and Class_4aac041b.Field_9540bd8e +1. Prior draw-step interpretation is retained as context; current selector owner/receiver and swap totals remain unresolved.

EA class guides support their own text and unlock levels, independently of UI/gameplay mapping. Duplicate ActiveFlak description identities remain separate. No new additional-family numeric interpretation or native formula is established.

L848 extends the soldier atlas with exact Feature_Soldier_Suppression â†’ PresEx_Suppression and current named spotting/suppression/mode setting definitions. PresEx member names are presentation structure, not gameplay effects. The spotting owner imports BR shakedown/spectator variants; exclude these from standard MP claims. SimEx mode inputs include GameMode, GameState, IsSP, IsQuickRespawn, HasModeTweaks, IsGranite and IsGauntlet. Mode root properties remain timeout-specific. Keep health/damage multipliers and revive/death defaults separate from active overrides. Reopen only on exact caller input values and a supported compiled-resource evaluator with same-owner control. Proposals and non-recording validation predictions are in l848-result.json.

L849 weapon movement and handling selections

All63 current WB raw hashes match the authoritative prior receipts. Current u32 rereads reproduce all ADS, sprint and DTA selections. The independent named ADS control uses the M433 owner/schema, exact registry wrapper, and child/hash pair.193 scalar reads stay within the200 cap.

| Weapon class | Count | ADS base ratio | Default sprint ms | Default deploy ms | Default holster ms |
|---|---:|---:|---:|---:|---:|
| Assault Rifle | 11 | 0.6Ã¢â‚¬â€œ0.6 | 166.667Ã¢â‚¬â€œ166.667 | 533.334Ã¢â‚¬â€œ533.334 | 200.001Ã¢â‚¬â€œ200.001 |
| Carbine | 9 | 0.67Ã¢â‚¬â€œ0.67 | 133.334Ã¢â‚¬â€œ133.334 | 466.667Ã¢â‚¬â€œ466.667 | 166.667Ã¢â‚¬â€œ166.667 |
| DMR | 6 | 0.475Ã¢â‚¬â€œ0.67 | 133.334Ã¢â‚¬â€œ233.334 | 466.667Ã¢â‚¬â€œ733.334 | 166.667Ã¢â‚¬â€œ266.667 |
| LMG | 10 | 0.475Ã¢â‚¬â€œ0.535 | 200.001Ã¢â‚¬â€œ266.667 | 633.334Ã¢â‚¬â€œ866.667 | 233.334Ã¢â‚¬â€œ300.001 |
| SMG | 10 | 0.745Ã¢â‚¬â€œ0.745 | 100.001Ã¢â‚¬â€œ100.001 | 400.001Ã¢â‚¬â€œ400.001 | 133.334Ã¢â‚¬â€œ133.334 |
| Shotgun | 4 | 0.6Ã¢â‚¬â€œ0.67 | 133.334Ã¢â‚¬â€œ166.667 | 466.667Ã¢â‚¬â€œ533.334 | 166.667Ã¢â‚¬â€œ200.001 |
| Sidearm | 7 | 0.745Ã¢â‚¬â€œ0.825 | 66.667Ã¢â‚¬â€œ100.001 | 200.001Ã¢â‚¬â€œ350.001 | 83.334Ã¢â‚¬â€œ166.667 |
| Sniper Rifle | 6 | 0.42Ã¢â‚¬â€œ0.67 | 133.334Ã¢â‚¬â€œ233.334 | 466.667Ã¢â‚¬â€œ633.334 | 166.667Ã¢â‚¬â€œ233.334 |

The table shows current site model ranges. Do not use class averages as source selectors. VZ61 retains the primary DTA table despite its Sidearm class. Deploy and sprint coordinates are independent.

M433 source bases select ADS0.6, sprint200.001 ms, deploy633.334 ms and undeploy233.334 ms. Its default30 Rnd magazine shifts sprint and deploy by-1, so the current model displays ADS0.60Ãƒâ€”, sprint167 ms, deploy533 ms and computed holster200 ms. Existing UI cards already display the first three. A separate Holster setting card can show the fourth, with a source-setting label.

A non-recording model check is saved: selecting M43320 Rnd gives ADS0.75Ãƒâ€”, sprint133 ms, deploy467 ms and holster167 ms with actual UI formatting. These are software predictions, not gameplay measurements.

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

The queue now has six proposals: the existing model's holster setting, plus guide-supported Quicker Recovery, Soft Landing, Revive Recovery, Explosives Resistant and Low Profile descriptions. Each proposal has a concrete prediction. Only the holster proposal has a validated software number: M433 30 Rnd gives 200 ms and 20 Rnd gives 167 ms. Source handling settings do not establish total swap time. Perk text can state the official guide effect after current UI selection verification; unresolved raw operands do not supply additional effective values.

The Season 5 preview describes its training-path changes within battle royale. Shared Common owners require an MP overlap check after the update. No specific MP numeric change is asserted. [Receipt](../../reference-data/provenance/frosty-2026-10-01-L861-limits-proposals-batch1.json).

L862 complete: exact spotting-to-OverlayPicker receiver qualified after the suppression PresEx positive control. Five presentation ports, local InLobby/Active states, and exact outgoing imports are retained.39 stored f32 values are raw checked but do not establish effective durations or ranges. Four owner files inspected. Multiplayer branch selection, native activation and gameplay detection remain unresolved. No site changes.
Current collection catalog resolves23 of27 outgoing import occurrences. Four occurrences across3 file GUIDs remain catalog gaps. Existing raw paths/hashes and same-owner control guidance appear in next-routes-v2.json. Use draft-receipt-v2.json and l862-result-v2.json.

L863 completed the fixed seven-row source scope. The independent FasterRegen control reproduced rate 30, delay 2.5 and amount 0. All eight incoming edges and target exports passed raw checks.

AntiRepair, ActiveRepair and Ulti_Consumed share a hash-only typed family. MechanicOverheat Stationaries/Vehicles share another family with false plus 0.5/0.9; these values have no qualified effect role. The two exact GRX children retain named scalar storage: Mine Sweep Radius 30 and DamageSpot_Duration 8. Units, tuple companions and native operations remain unresolved. No hardware exclusion or gameplay formula follows.

Eight bodies were decoded. Incoming SimEx receipts were reread at selected fields only. No vehicle/gadget bodies, captures, repository changes or site changes were made. No generated output exceeds 50 MB. See family-atlas.json, raw checks, next-routes.json and draft-receipt.json.

L864 complete. Controls pass. 132 scoped owners (136 with original UI owners), 1899 typed families and 25243 numeric observations. All14 captured-only body gaps close. All32 slots/28 Ability targets retain source dispositions. Canonical L860/L862/L863 integrated. 476 new physical reads; 1088 extension reads reused. No source role or native activation inferred. L865 remains pending:27 outgoing occurrences and3 file-GUID index gaps. Original and L859 atlas snapshots unchanged.

Use soldier-atlas-frontier-v3.json for this snapshot. Source closure is separate from native meaning. Keep L865 exact selected receiver pass open; do not label the frontier exhausted.

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

Six queue proposals remain reviewable: holster setting plus five official-guide perk descriptions. M433 30 Rnd predicts holster 200 ms; 20 Rnd predicts 167 ms. Each proposal has a non-recording validation prediction. Guide descriptions require current UI selection verification before binding. The Season 5 preview puts training changes in battle royale; shared Common source overlap is an MP recheck risk.

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
