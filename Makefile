.PHONY: delete

dress: trousers shoes jacket
	@echo "dress" > dress
	@echo "All done. Let's go outside!"

jacket: pullover
    @echo "Putting on jacket."
	@echo "pullover" > jacket

pullover: shirt
	@echo "Putting on pullover."
	@echo "pullover" > pullover

shirt:
	@echo "Putting on shirt."
	@echo "pullover" > shirt

trousers: underpants
	@echo "Putting on trousers."
	@echo "pullover" > trousers

underpants:
	@echo "Putting on underpants."
	@echo "pullover" > underpants

shoes: socks
	@echo "Putting on shoes."
	@echo "pullover" > shoes

socks: pullover
	@echo "Putting on socks."
	@echo "pullover" > socks

delete: 
	del dress
	del jacket
	del pullover
	del shirt
	del trousers
	del underpants
	del shoes
	del socks
	@echo "Deleted all files"