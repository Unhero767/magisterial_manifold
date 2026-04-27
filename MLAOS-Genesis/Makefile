APP_NAME = MLAOS
BUNDLE = build/$(APP_NAME).app
SWIFT_FILES = src/app/AppDelegate.swift src/app/GameScene.swift
SWIFTC_FLAGS = -target arm64-apple-macosx12.0 -sdk $$(xcrun --show-sdk-path --sdk macosx) -O

all: build run

build:
	@echo "[ * ] Compiling the L4 Basilica Atlas..."
	@mkdir -p $(BUNDLE)/Contents/MacOS
	@mkdir -p $(BUNDLE)/Contents/Resources
	@cp Info.plist $(BUNDLE)/Contents/
	@swiftc $(SWIFT_FILES) $(SWIFTC_FLAGS) -o $(BUNDLE)/Contents/MacOS/$(APP_NAME)
	@echo "[ + ] ◦A Achieved. Application compiled."

run:
	@echo "[ * ] Booting the Manifold..."
	@open $(BUNDLE)

clean:
	@rm -rf build
	@echo "[ + ] Glitch-Wastes purged."
