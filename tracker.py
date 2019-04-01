# white items
soldiers_syringe = 0
tougher_times = 0
monster_tooth = 0
lens_makers_glasses = 0
pauls_goat_hoof = 0
bustling_fungus = 0
crowbar = 0
tri_tip_dagger = 0
warbanner = 0
cautious_slug = 0
personal_shield_generator = 0
medkit = 0
gasoline = 0
stun_grenade = 0
bundle_of_fireworks = 0
energy_drink = 0
backup_magazine = 0
sticky_bomb = 0
rusted_key = 0
armor_piercing_rounds = 0

# green items
atg_missile_mk_1 = 0
will_o_the_wisp = 0
hopoo_feather = 0
ukelele = 0
leeching_seed = 0
predatory_instincts = 0
red_whip = 0
old_war_stealthkit = 0
harvesters_scythe = 0
fuel_cell = 0
infusion = 0
bandolier = 0
berzerkers_pauldron = 0
rose_buckler = 0
runalds_band = 0
kjaros_band = 0
chronobauble = 0
wax_quail = 0

# red items
brilliant_behemoth = 0
ceremonial_dagger = 0
frost_relic = 0
happiest_mask = 0
h3ad_st_v2 = 0
nkuhanas_opinion = 0
unstable_tesla_coil = 0
fiftyseven_leaf_clover = 0
sentient_meat_hook = 0
alien_head = 0
soulbound_catalyst = 0
dios_best_friend = 0
hardlight_afterburner = 0
wake_of_vultures = 0
brainstalks = 0
rejuvenation_rack = 0

# yellow items
titanic_knurl = 0
queens_gland = 0

# blue items
shaped_glass = 0
brittle_crown = 0
transcendence = 0
corpsebloom = 0
gesture_of_the_drowned = 0
glowing_meteorite = 0
hellfire_tincture = 0
effigy_of_grief = 0

# overall stats
attack_speed = 100
critical_strike = 100


def main():
    global attack_speed
    global critical_strike

    print("GENERAL:")
    if soldiers_syringe > 0:
        atk_spd = 15*soldiers_syringe
        print("Increases attack speed by " + str(atk_spd) + "%.")
        attack_speed = attack_speed + atk_spd
    if crowbar > 0:
        damage = 150 + 30*(crowbar - 1)
        print("Deal " + str(damage) + "% damage to enemies above 90% health")
    if warbanner > 0:
        banner_distance = 16 + 8*(warbanner - 1)
        print("On level up drop a banner that strengthens all allies within " + str(banner_distance) + "m. Raise attack and movement speed by 30%")
    if personal_shield_generator > 0:
        health_shield = 25*personal_shield_generator
        print("Gain a " + str(health_shield) + "-health shield. Recharges outside of danger.")
    if bundle_of_fireworks > 0:
        firework_num = 8 + 4*(bundle_of_fireworks - 1)
        print("Opening a chest launches " + str(firework_num) + " fireworks that deal 300% base damage.")
    if energy_drink > 0:
        sprint_speed = 30 + 20*(energy_drink - 1)
        print("Sprint speed is improved by " + str(sprint_speed) + "%.")
    if backup_magazine > 0:
        print("Add +" + str(backup_magazine) + " charge to your Secondary skill.")
    if armor_piercing_rounds > 0:
        boss_damage = 20 + 10*(armor_piercing_rounds - 1)
        print("Deal an additional " + str(boss_damage) + "% damage to bosses.")
    if atg_missile_mk_1 > 0:
        missile_damage = 300*atg_missile_mk_1
        print("10% chance to fire a missile that deals " + str(missile_damage) + "% damage.")
    if ukelele > 0:
        ukelele_targets = 3 + 2*(ukelele - 1)
        ukelele_range = 20 + 2*(ukelele - 1)
        print("25% chance to fire chain lightning for 80% damage on up to " + str(ukelele_targets) + " targets within " + str(ukelele_range) + "m.")
    if predatory_instincts > 0:
        max_attack_speed = 30*predatory_instincts
        print("Critical strikes increase attack speed by 10%. Maximum cap of " + str(max_attack_speed) + "% attack speed.")
    if harvesters_scythe > 0:
        critical_heal = 8 + 4*(harvesters_scythe - 1)
        print("Gain 5% critical chance. Critical strikes heal for " + str(critical_heal) + " health.")
        critical_strike = critical_strike + 5
    if fuel_cell > 0:
        equipment_cooldown = 15*fuel_cell
        print("Hold " + str(fuel_cell) + " additional equipment charges. Reduce equipment cooldown by " + str(equipment_cooldown) + "%.")
    if rose_buckler > 0:
        armor = 25*rose_buckler
        print("Increase armor by " + str(armor) + " while sprinting.")
    if wax_quail > 0:
        jump_distance = 10 * wax_quail
        print("Jumping while sprinting boosts you forward by " + str(jump_distance) + "m.")
    if brilliant_behemoth > 0:
        explode_radius = 4 + 1.5*(brilliant_behemoth)
        print("All of your attacks explode in a " + str(explode_radius) + "m radius for a bonus 60% damage to nearby enemies.")
    if h3ad_st_v2 > 0:
        recharge_time = 10 - 5*(h3ad_st_v2 - 1)
        print("Increase jump height. Creates a 10m radius kenetic explosion on hitting the ground, dealing 2300% base damage that scales up with speed. Recharges in " + str(recharge_time) + "s.")
    if nkuhanas_opinion > 0:
        soul_energy_percent = 100 * nkuhanas_opinion
        print("Store " + str(soul_energy_percent) + "% of healing as Soul Energy. After your Soul Energy reaches 10% of your maximum health, fire a skull that deals 250% of your Soul Energy as damage.")
    if unstable_tesla_coil > 0:
        tesla_enemies_hit = 3*unstable_tesla_coil
        print("Fire out lightning that hits " + str(tesla_enemies_hit) + " enemies for 200% base damage every 0.5 seconds. The Tesla Coil switches off every 10 seconds.")
    if fiftyseven_leaf_clover > 0:
        print("All random effects are rolled " + str(fiftyseven_leaf_clover) + " times for a more favorable outcome.")
    if alien_head > 0:
        skill_cooldown = 25*alien_head
        print("Reduce skill cooldowns by " + str(skill_cooldown) + "%.")
    if hardlight_afterburner > 0:
        utility_skills = 2*hardlight_afterburner
        print("Add +" + str(utility_skills) + " charges to your Utility skill. Reduces Utility skill cooldown by 33%.")
    if rejuvenation_rack > 0:
        healing_received = 100*rejuvenation_rack
        print("Increase all healing received by " + str(healing_received) + "%.")
    if pauls_goat_hoof > 0:
        movement_speed = 14*pauls_goat_hoof
        print("Increases movement speed by " + str(movement_speed) + "%.")
    if bustling_fungus > 0:
        heals = 4.5 + 2.25*(bustling_fungus - 1)
        radius = 3 + 1.5*(bustling_fungus - 1)
        print("After standing still for 2 seconds, create a zone that heals for " + str(heals) + "% of your health every second to all allies within " + str(radius) + "m.")
    if hopoo_feather > 0:
        print("Gain +" + str(hopoo_feather) + " maximum jump count.")
    if rusted_key > 0:
        print("A hidden cache containing an item will appear in a random location in each stage.")

    # print overall stats
    print()
    print("OVERALL STATS:")
    print("Attack speed: " + str(attack_speed) + "%")
    print("Critical strike: " + str(critical_strike) + "%")

    print("")

    print("ON HITTING ENEMY:")
    if lens_makers_glasses > 0:
        atk_chance = 10*lens_makers_glasses
        print("Your attacks have a " + str(atk_chance) + "% chance to 'Critically Strike', dealing double damage.")
        critical_strike = critical_strike + atk_chance
    if tri_tip_dagger > 0:
        bleed_chance = 15 + 15*(tri_tip_dagger - 1)
        print(str(bleed_chance) + "% chance to bleed an enemy for 240% base damage")
    if sticky_bomb > 0:
        bomb_chance = 5 + 2.5*(sticky_bomb - 1)
        detonate_damage = 250 + 125*(sticky_bomb - 1)
        print(str(bomb_chance) + "% chance on hit to attach a bomb to an enemy, detonating for " + str(detonate_damage) + "% damage.")
    if runalds_band > 0:
        runalds_damage = 250 + 125*(runalds_band - 1)
        print("8% chance on hit to strike an enemy with a runic ice blast, slowing them by 80% and dealing " + str(runalds_damage) + "% damage.")
    if kjaros_band > 0:
        kjaros_damage = 500 + 250*(kjaros_band - 1)
        print("8% chance on hit to strike an enemy with a runic flame tornado, dealing " + str(kjaros_damage) + "% damage.")
    if chronobauble > 0:
        print("Slow enemies on hit for -60% movement speed for " + str(chronobauble) + "s.")
    if leeching_seed > 0:
        print("Dealing damage heals you for " + str(leeching_seed) + " health.")
    if stun_grenade > 0:
        stun_chance = 5*stun_grenade
        print(str(stun_chance) + "% chance on hit to stun enemies for 2 seconds.")
    if sentient_meat_hook > 0:
        hook_chance = 20*sentient_meat_hook
        hook_stack = 10 + 5*(sentient_meat_hook-1)
        print(str(hook_chance) + "% chance on hit to fire homing hooks at up to " + str(hook_stack) + " enemies for 100% damage.")

    print()
    print("ON KILL:")
    if monster_tooth > 0:
        healing_orb = 10 + 5*(monster_tooth - 1)
        print("Killing an enemy spawns a healing orb that heals for " + str(healing_orb) + " health.")
    if gasoline > 0:
        burn_radius = 12 + 4*(gasoline - 1)
        burn_damage = 150 + 75*(gasoline - 1)
        print("Killing an enemy ignites all enemies within " + str(burn_radius) + "m. Enemies burn for " + str(burn_damage) + "% base damage.")
    if will_o_the_wisp > 0:
        pillar_radius = 12 + 2.4*(will_o_the_wisp - 1)
        pillar_damage = 350 + 280*(will_o_the_wisp - 1)
        print("On killing an enemy, spawn a lava pillar in a " + str(pillar_radius) + "m radius for " + str(pillar_damage) + "% base damage.")
    if infusion > 0:
        health_max = 100 * infusion
        print("Killing an enemy increases your health permanently by 1, up to a maximum of " + str(health_max) + " health.")
    if bandolier > 0:
        chance_to_reset_cooldown = 18 + 10*(bandolier - 1)
        print(str(chance_to_reset_cooldown) + "% chance on kill to drop an ammo pack that resets all cooldowns.")
    if berzerkers_pauldron > 0:
        berzerkers_time = 6 + 4*(berzerkers_pauldron - 1)
        print("Killing 3 enemies within 1 second sends you into a frenzy for " + str(berzerkers_time) + "s. Increases movement speed by 50% and attack speed for 100% for the duration.")
    if ceremonial_dagger > 0:
        print("Killing an enemy releases homing daggers.")
    if frost_relic > 0:
        print("Killing an enemy surrounds you with icicles that deal 3x33% damage.")
    if happiest_mask > 0:
        mask_time = 30*happiest_mask
        print("Killing enemies has a 10% chance to spawn a ghost of the killed enemy with 500% damage. Lasts " + str(mask_time) + "s.")
    if soulbound_catalyst > 0:
        reduce_equipment_cooldown = 4 + 2*(soulbound_catalyst - 1)
        print("Kills reduce equipment cooldown by " + str(reduce_equipment_cooldown) + "s.")
    if wake_of_vultures > 0:
        wake_seconds = 8 + 5*(wake_of_vultures - 1)
        print("Gain the power of any killed elite monster for " + str(wake_seconds) + "s.")
    if brainstalks > 0:
        frenzy_time = 3 + 2*(brainstalks - 1)
        print("Upon killing an elite monster, enter a frenzy for " + str(frenzy_time) + "s where skills have no cooldowns.")

    print()
    print("OUT OF COMBAT:")
    if cautious_slug > 0:
        passive_health_regen = 250 + 150*(cautious_slug - 1)
        print("Increases passive health regeneration by " + str(passive_health_regen) + "% while outside of combat.")
    if red_whip > 0:
        out_of_combat_speed = 30*red_whip
        print("Leaving combat boosts your movement speed by " + str(out_of_combat_speed) + "%.")

    print()
    print("ON GETTING HIT:")
    if tougher_times > 0:
        block_chance = 100 + (1 - (1/(0.15*(tougher_times + 1))) * 100)
        print(str(block_chance) + "% chance to block incoming damage. Unaffected by luck.")
    if medkit > 0:
        heal = 10*medkit
        print("Heal for " + str(heal) + " health 1.1 seconds after getting hurt.")
    if old_war_stealthkit > 0:
        invisibility_duration = 3 + 1.5*(old_war_stealthkit - 1)
        print("Chance on taking damage to gain 40% movement speed and invisibility for " + str(invisibility_duration) + "s. Chance increases the more damage you take.")
    if dios_best_friend > 0:
        print("Upon death, this item will be consumed and you will return to life with 3 seconds of invulnerability.")


if __name__ == "__main__":
    main()
