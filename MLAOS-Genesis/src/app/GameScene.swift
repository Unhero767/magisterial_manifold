import SpriteKit

public class GameScene: SKScene {
    private var aureliaNode: SKSpriteNode!
    private var zkPerimeter: SKShapeNode!
    private var statusLabel: SKLabelNode!
    
    override public func didMove(to view: SKView) {
        self.anchorPoint = CGPoint(x: 0.5, y: 0.5)
        self.backgroundColor = NSColor(red: 0.1, green: 0.1, blue: 0.15, alpha: 1.0) // Brighter void
        
        // VISUAL ANCHOR: If you see this text, the L4 Basilica is rendering properly.
        statusLabel = SKLabelNode(text: "[ SECTOR-01 : STANDBY ]")
        statusLabel.fontName = "Courier"
        statusLabel.fontSize = 24
        statusLabel.fontColor = .white
        statusLabel.position = CGPoint(x: 0, y: 200)
        self.addChild(statusLabel)
        
        zkPerimeter = SKShapeNode(circleOfRadius: 120)
        zkPerimeter.strokeColor = NSColor.red
        zkPerimeter.lineWidth = 4.0
        zkPerimeter.alpha = 0.0
        self.addChild(zkPerimeter)
        
        // Brighter idle morphotype
        aureliaNode = SKSpriteNode(color: NSColor.lightGray, size: CGSize(width: 40, height: 80))
        self.addChild(aureliaNode)
    }
    
    public func triggerCombatProtocol() {
        statusLabel.text = "[ THREAT CRITICAL : Zk PERIMETER ACTIVE ]"
        statusLabel.fontColor = .red
        
        zkPerimeter.alpha = 1.0
        let expand = SKAction.scale(to: 1.1, duration: 0.5)
        let contract = SKAction.scale(to: 1.0, duration: 0.5)
        zkPerimeter.run(SKAction.repeatForever(SKAction.sequence([expand, contract])), withKey: "pulse")
        
        aureliaNode.color = NSColor.cyan
    }
    
    public func enforceStandDown() {
        statusLabel.text = "[ SECTOR-01 : SECURE ]"
        statusLabel.fontColor = .white
        
        zkPerimeter.removeAction(forKey: "pulse")
        zkPerimeter.alpha = 0.0
        aureliaNode.color = NSColor.lightGray
    }
}
