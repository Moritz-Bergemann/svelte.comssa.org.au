<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	let scrollY: number;
	onMount(() => {
		
	});
</script>

<div class="navbar-placeholder">

</div>

<div class="navbar {scrollY > 0 ? "active-navbar": ""}">
	<div class="navbar-items">
		<a href="www.beans.com" class="navbar-item underlined"><span class="underline">Contact</span></a>
		<a href="www.beans.com" class="navbar-item underlined"><span class="underline">Events</span></a>
		<a class="{scrollY < 250 ? "hidden" : ""}"><img src="/assets/comssa-c.png"/></a>
		<a href="www.beans.com" class="navbar-item underlined"><span class="underline">Meeting Minutes</span></a>
		<a href="www.beans.com" class="navbar-item underlined"><span class="underline">Sponsors</span></a>
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
		border-bottom: solid thick var(--comssa-blue);
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

	.navbar-items a {
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
