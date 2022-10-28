
# Uplink-Desktop CSS Test Bench
- This project uses [bottle](https://bottlepy.org/docs/dev/tutorial.html#installation) which can be installed via `pip` or the `bottle.py` file can be used on its own. 
- You should be able to run `./server.py`, go to `localhost:8080`, and view your web page there. You can change the HTMl or CSS files, refresh the page, and see the changes instantly. 

## Rationale
- Testing CSS changes on Uplink Desktop takes too long so this project aims to provide a testbench allowing fast iteration.
- Last time someone tried Dioxus hot-reload, they found that the app recompiled with every change within the rsx! macro. Plus dioxus takes a long time to compile and link. 
