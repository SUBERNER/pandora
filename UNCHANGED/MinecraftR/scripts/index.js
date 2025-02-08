import { system, world } from '@minecraft/server'
import { MinecraftItemTypes } from './items'
import { ActionFormData, ModalFormData } from '@minecraft/server-ui';

const board = "RANDOMitems"
const settingsBoard = "RANDOMsettings"
const itemTypes = Object.values(MinecraftItemTypes);
var itemsRandomized = {}
var chosenRandomly = []

world.getDimension("overworld").runCommand("gamerule dotiledrops false")

var allowDiscs = false
var allowElements = false
var allowSpawnEggs = false
var allowBanner = false
var allowBoats = false
var allowSmithingTemplate = false
var allowPotterySherd = false
var allowCreativeItems = false
var creativeItems = [
    "minecraft:command_block",
    "minecraft:command_block_cart",
    "minecraft:repeating_command_block",
    "minecraft:chain_command_block",
    "minecraft:barrier",
    "minecraft:jigsaw",
    "minecraft:structure_block",
    "minecraft:allow",
    "minecraft:deny",
    "minecraft:light_block",
    "minecraft:structure_void"
]

function spawnItem(itemId, location, player) {
    let x = location.x
    let y = location.y
    let z = location.z
    if (player.runCommand("testforblock ~~100~ air").successCount) {
        y += 100
        player.runCommand(`setblock ${x} ${y} ${z} chest`)
        player.runCommand(`replaceitem block ${x} ${y} ${z} slot.container 0 ${itemId}`)
        player.runCommand(`setblock ${x} ${y} ${z} chest destroy`)
        player.runCommand(`kill @e[x=${x}, y=${y}, z=${z}, type=item, name=Chest, c=1]`)
        player.runCommand(`tp @e[type=item, x=${x}, y=${y}, z=${z}, c=1] ${x} ${location.y} ${z}`)
        player.runCommand(`setblock ${x} ${y} ${z} air replace`)
    } else {
        player.runCommand(`setblock ${x} ${y} ${z} chest`)
        player.runCommand(`replaceitem block ${x} ${y} ${z} slot.container 0 ${itemId}`)
        player.runCommand(`setblock ${x} ${y} ${z} chest destroy`)
        player.runCommand(`kill @e[x=${x}, y=${y}, z=${z}, type=item, name=Chest, c=1]`)
        player.runCommand(`setblock ${x} ${y} ${z} air replace`)
    }
}

function getRandomItem() {
    return itemTypes[Math.floor(Math.random() * itemTypes.length)]
}

system.runTimeout(() => {
    world.sendMessage("§aYou are currently using Minecraft Randomizer!")
    world.sendMessage("§aTo open the script's menu, type in the following command:")
    world.sendMessage("§e/scriptevent rnd:ui")
}, 20)

world.afterEvents.worldInitialize.subscribe(o => {
    if (!world.scoreboard.getObjective(board)) {
        // First load
        world.scoreboard.addObjective(board)
        world.scoreboard.addObjective(settingsBoard)
        let settings = world.scoreboard.getObjective(settingsBoard)
        settings.addScore("allowDiscs", allowDiscs)
        settings.addScore("allowElements", allowElements)
        settings.addScore("allowSpawnEggs", allowSpawnEggs)
        settings.addScore("allowBanner", allowBanner)
        settings.addScore("allowBoats", allowBoats)
        settings.addScore("allowSmithingTemplate", allowSmithingTemplate)
        settings.addScore("allowPotterySherd", allowPotterySherd)
        settings.addScore("allowCreativeItems", allowCreativeItems)
    } else {
        // Load items
        world.scoreboard.getObjective(board).getParticipants().forEach(item => {
            itemsRandomized[item.displayName.split("$")[0]] = item.displayName.split("$")[1]
            chosenRandomly.push(item.displayName.split("$")[1])
        })
        world.scoreboard.getObjective(settingsBoard).getScores().forEach(setting => {
            if (setting.participant.displayName == "allowDiscs") allowDiscs = !!setting.score
            if (setting.participant.displayName == "allowElements") allowElements = !!setting.score
            if (setting.participant.displayName == "allowSpawnEggs") allowSpawnEggs = !!setting.score
            if (setting.participant.displayName == "allowBanner") allowBanner = !!setting.score
            if (setting.participant.displayName == "allowBoats") allowBoats = !!setting.score
            if (setting.participant.displayName == "allowSmithingTemplate") allowSmithingTemplate = !!setting.score
            if (setting.participant.displayName == "allowPotterySherd") allowPotterySherd = !!setting.score
            if (setting.participant.displayName == "allowCreativeItems") allowCreativeItems = !!setting.score
        })
    }
})

world.beforeEvents.playerBreakBlock.subscribe(o => {
    o.player.brokenBlock = o.block.typeId
})

world.afterEvents.playerBreakBlock.subscribe(o => {
    let brokenBlock = o.player.brokenBlock
    if (!itemsRandomized[brokenBlock]) {
        let randomItem = getRandomItem()
        while (true) {
            if (randomItem in chosenRandomly ||
                (allowDiscs === false && randomItem.startsWith("minecraft:music_disc")) ||
                (allowElements === false && randomItem.startsWith("minecraft:element")) ||
                (allowSpawnEggs === false && randomItem.endsWith("spawn_egg")) ||
                (allowBanner === false && randomItem.endsWith("banner_pattern")) ||
                (allowBoats === false && randomItem.endsWith("boat")) ||
                (allowSmithingTemplate === false && randomItem.endsWith("smithing_template")) ||
                (allowPotterySherd === false && randomItem.endsWith("pottery_sherd")) ||
                (randomItem == "minecraft:bundle")
            ) {
                // Did not pass
                randomItem = getRandomItem()
                continue

            } else {
                let pass = true

                // Special check for creative items
                if (allowCreativeItems === false) {
                    creativeItems.forEach(item => {
                        if (randomItem.startsWith(item) || randomItem.endsWith(item)) {
                            pass = false
                        }
                    })
                } 

                if (pass) {
                    // Passed all checks
                    chosenRandomly.push(randomItem)
                    itemsRandomized[brokenBlock] = randomItem
                    break
                } else {
                    // Did not pass creative items check
                    randomItem = getRandomItem()
                    continue    
                }
            }
        }
        world.scoreboard.getObjective(board).addScore(brokenBlock + "$" + randomItem, 0)
    }
    spawnItem(itemsRandomized[brokenBlock], o.block.location, o.player)
})

system.afterEvents.scriptEventReceive.subscribe(o => {
    if (o.id == "rnd:ui") {
        let form = new ActionFormData()
        form.title("Randomizer Menu")
        form.body("Select an option")
        form.button("Search Block Drops")
        form.button("Randomizer Settings")
        form.button("Reset Block Drops")
        form.button("Exit")
        form.show(o.sourceEntity).then(response => {
            if (response.selection == 0) { // Search
                let result = undefined
                let searchTerm
                let form = new ActionFormData()
                form.title("Randomizer Menu - Search")
                form.body("Select an option")
                form.button("Search by Identifier")
                form.button("List of Items Randomized")
                form.show(o.sourceEntity).then(srchValue => {
                    if (srchValue.selection == 0) {
                        let form = new ModalFormData()
                        form.title("Randomizer Menu - Search by Id")
                        form.textField("Search for an item's identifier to get the corresponding random item drop (that you have already unlocked)", "Ex. grass_block")
                        form.submitButton("Search")
                        form.show(o.sourceEntity).then(formValues => {
                            searchTerm = formValues.formValues[0]
                            for (let block in itemsRandomized) {
                                if (block.split(":")[1] == searchTerm) {
                                    result = itemsRandomized[block].split(":")[1]
                                    world.sendMessage("§a" + searchTerm + " gives: " + result)
                                    world.playSound("random.orb", o.sourceEntity.location)
                                }
                            }
                            if (!result) {
                                world.sendMessage("§cSearch term was not found")
                            }
                        })
                    } else if (srchValue.selection == 1) {
                        let form = new ActionFormData()
                        form.title("Randomizer Menu - List of Items")
                        let txt = ""
                        for (let block in itemsRandomized) {
                            txt += block.split(":")[1] + " -> " + itemsRandomized[block].split(":")[1] + "\n" + "<--==[]==-->" + "\n"
                        }
                        form.body(txt)
                        form.button("Exit")
                        form.show(o.sourceEntity).then(p =>{})
                    }
                })

            } else if (response.selection == 1) { // Settings
                form = new ModalFormData()
                form.title("Randomizer Menu - Settings")
                form.toggle("Allow Music Discs", allowDiscs)
                form.toggle("Allow Elements", allowElements)
                form.toggle("Allow Spawn Eggs", allowSpawnEggs)
                form.toggle("Allow Banners", allowBanner)
                form.toggle("Allow Boats", allowBoats)
                form.toggle("Allow Smithing Templates", allowSmithingTemplate)
                form.toggle("Allow Potter Sherds", allowPotterySherd)
                form.toggle("Allow Creative Mode Items", allowCreativeItems)
                form.submitButton("Save Changes")
                form.show(o.sourceEntity).then(formValues => {
                    allowDiscs = formValues.formValues[0]
                    allowElements = formValues.formValues[1]
                    allowSpawnEggs = formValues.formValues[2]
                    allowBanner = formValues.formValues[3]
                    allowBoats = formValues.formValues[4]
                    allowSmithingTemplate = formValues.formValues[5]
                    allowPotterySherd = formValues.formValues[6]
                    allowCreativeItems = formValues.formValues[7]
                    let settings = world.scoreboard.getObjective(settingsBoard)
                    settings.setScore("allowDiscs", allowDiscs)
                    settings.setScore("allowElements", allowElements)
                    settings.setScore("allowSpawnEggs", allowSpawnEggs)
                    settings.setScore("allowBanner", allowBanner)
                    settings.setScore("allowBoats", allowBoats)
                    settings.setScore("allowSmithingTemplate", allowSmithingTemplate)
                    settings.setScore("allowPotterySherd", allowPotterySherd)
                    settings.setScore("allowCreativeItems", allowCreativeItems)
                })
            } else if (response.selection == 2) { // Reset
                itemsRandomized = {}
                chosenRandomly = []
                world.scoreboard.removeObjective(board)
                world.scoreboard.addObjective(board)
            }
        })
    }
})