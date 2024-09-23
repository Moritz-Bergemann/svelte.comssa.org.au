<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import { fly } from 'svelte/transition';
	import NavBarContent from './NavBarContent.svelte';
	import Page from '../../../routes/contact/+page.svelte';
	export let followScroll: boolean = true;
	export let showCAlways: boolean = false;
	let scrollY: number;
</script>

<div class="navbar navbar-static">
	<NavBarContent showC={showCAlways}/>
</div>

{#if followScroll && scrollY > 300}
	<div
		in:fly|global={{ y: -75, opacity: 1, duration: 500 }}
		out:fly|global={{ y: -75, opacity: 1, duration: 250 }}
		class="navbar navbar-follow"
	>
		<NavBarContent showC={true}/>
	</div>
{/if}

<svelte:window bind:scrollY />

<style>
	.navbar {
		width: 100vw;
		z-index: 100;
		text-align: center;
		top: 0;
		background-color: white;
	}

	.navbar-static {
		height: 75px;
		max-height: 150px;
	}

	.navbar-follow {
		position: fixed;
		height: 75px;
		box-shadow: 0px 0px 10px 5px rgba(128, 128, 128, 0.25);;
        
	}
</style>
