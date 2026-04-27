import Cocoa
import SpriteKit

@main
class AppDelegate: NSObject, NSApplicationDelegate {
    var window: NSWindow!
    var skView: SKView!
    private var ledgerWatcher: DispatchSourceFileSystemObject?
    
    private let ledgerPath = FileManager.default.homeDirectoryForCurrentUser
        .appendingPathComponent("MLAOS-Genesis/src/data/reality_state.json")

    func applicationDidFinishLaunching(_ aNotification: Notification) {
        // Force the app to become a regular foreground app
        NSApp.setActivationPolicy(.regular)
        
        let screenSize = NSRect(x: 0, y: 0, width: 1024, height: 768)
        window = NSWindow(contentRect: screenSize, styleMask: [.titled, .closable, .miniaturizable, .resizable], backing: .buffered, defer: false)
        window.title = "L4 Basilica Atlas: Sector-01 (Olney Anchor)"
        window.center()
        
        skView = SKView(frame: screenSize)
        skView.autoresizingMask = [.width, .height]
        window.contentView = skView
        
        let scene = GameScene(size: screenSize.size)
        scene.scaleMode = .aspectFill
        skView.presentScene(scene)
        
        window.makeKeyAndOrderFront(nil)
        NSApp.activate(ignoringOtherApps: true)
        
        awakenLedgerWatcher(scene: scene)
    }

    private func awakenLedgerWatcher(scene: GameScene) {
        if !FileManager.default.fileExists(atPath: ledgerPath.path) {
            try? "{}".write(to: ledgerPath, atomically: true, encoding: .utf8)
        }
        let fileDescriptor = open(ledgerPath.path, O_EVTONLY)
        guard fileDescriptor != -1 else { return }
        
        ledgerWatcher = DispatchSource.makeFileSystemObjectSource(fileDescriptor: fileDescriptor, eventMask: [.write, .extend, .attrib], queue: DispatchQueue.global(qos: .background))
        ledgerWatcher?.setEventHandler { [weak self] in
            self?.parseRealityState(for: scene)
        }
        ledgerWatcher?.resume()
    }
    
    private func parseRealityState(for scene: GameScene) {
        do {
            let data = try Data(contentsOf: ledgerPath)
            if let state = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any] {
                DispatchQueue.main.async {
                    if state["encounter_active"] as? Bool == true {
                        scene.triggerCombatProtocol()
                    } else {
                        scene.enforceStandDown()
                    }
                }
            }
        } catch { }
    }
}
