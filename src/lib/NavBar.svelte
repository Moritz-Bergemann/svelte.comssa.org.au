<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import { fade } from 'svelte/transition';
	export let dynamic: boolean = false;
	let scrollY: number;
	onMount(() => {
		
	});
</script>

<div class="navbar-placeholder">

</div>

<div class="navbar {!dynamic || scrollY > 0 ? "active-navbar": ""}">
	<div class="navbar-items">
		<a href="contact" class="navbar-item underlined"><span class="underline">Contact</span></a>
		<a href="events" class="navbar-item underlined"><span class="underline">Events</span></a>
		<div class="navbar-item">
			{#if !dynamic || scrollY < 250}
			<a in:fade out:fade href="/"><img alt="ComSSA" src="/assets/comssa-c.png"/></a>
			{/if}
		</div>
		<a href="https://drive.google.com/drive/folders/1HC9XAeFVHCOfjcJeRfK9hbmzNI1Ux2JX" class="navbar-item underlined"><span class="underline">Meeting Minutes</span></a>
		<a href="sponsors" class="navbar-item underlined"><span class="underline">Sponsors</span></a>
	</div>
</div>

<svelte:window bind:scrollY={scrollY} />

<style>
	.hidden {
		visibility: hidden;
	}
	
	.navbar-placeholder {
		width: 100vw;
		height: 75px;
	}

	.navbar {
		width: 100vw;
		height: 75px;
		z-index: 100;
		text-align: center;
		position: fixed;
		top: 0;
		background-color: white;
		box-shadow: gray;
		/* text-decoration: underline; */
		/* background-color: #4459a5; */
	}

	.active-navbar {
		border-bottom: solid var(--comssa-secondary-blue);
		opacity: 100%;
	}

	.navbar-items {
		padding-left: 10%;
		padding-right: 10%;
		height: 100%;
		display: flex;
		text-decoration: none;
		flex-direction: row;
		align-items: center;
	}

	.navbar-items .navbar-item {
		max-width: 150px;
		font-family: 'WaveHaus SemiBold';
		display: block;
		flex: auto;
		margin-left: auto;
		margin-right: auto;
		text-align: center;
		color: black;
		text-decoration: none;
	}

	.navbar-items a img {
		height: 50px;
	}

	.underlined::after {
		content: '';
		float: left;
		background: var(--comssa-blue);
		width: 100%;
		height: 0.2rem;
		border-radius: 5px;
		margin-top: 2px;
	}

	.underlined:hover:after {
		background:  var(--comssa-orange);
		transition: 0.3s;
	}
</style>
