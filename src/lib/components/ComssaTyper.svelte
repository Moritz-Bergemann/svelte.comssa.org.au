<script lang="ts">
import { onMount, onDestroy } from "svelte";
import TypeIt from "typeit";

let typerElement: HTMLElement;

onMount(() => {
	typerElement.innerHTML = "";

	let startingText = `<span class="comssa-blue-text" style="position: relative; top: 1rem;">~</span><span class="comssa-blue-text">/Com</span>
			<span class="comssa-blue-text">S</span>
			<span class="comssa-blue-text">S</span>
			<span class="comssa-blue-text">A</span>`;

	new TypeIt("#comssa-typer", {
		speed: 50,
		startDelay: 0,
		cursorChar: "_",
	})
		.type(startingText, { instant: true })
		.pause(1500)
		.move(-5, { instant: true })
		.pause(100)
		.move(-5, { instant: true })
		.pause(100)
		.move(-5, { instant: true })
		.pause(100)
		.type("puter ")
		.move(5, { instant: true })
		.type("cience ")
		.move(5, { instant: true })
		.type("tudents ")
		.move(5, { instant: true })
		.type("ssociation")
		.go();
});
</script>

<div class="comssa-typer" id="comssa-typer" bind:this={typerElement}>
	<span class="comssa-blue-text" style="position: relative; top: 1rem;">~</span>
	<span class="comssa-blue-text">/Com</span>
	<span class="comssa-blue-text">S</span>
	<span class="comssa-blue-text">S</span>
	<span class="comssa-blue-text">A</span>
</div>

<style>
	:root {
		--comssa-blue: #4459a5;
		--comssa-secondary-blue: #7ea3cc;
		--comssa-orange: #f5831f;
		--comssa-black: #404040;
	}

	.comssa-typer {
		font-family: WaveHaus Bold;
		text-align: center;
		font-size: 4rem;
		--ti-cursor-color: var(--text-color);
	}

	div .comssa-blue-text {
		color: var(--comssa-blue);
	}
</style>
