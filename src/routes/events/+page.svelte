<script lang="ts">
	import NavBar from '$lib/components/NavBar/NavBar.svelte';
	import EventCarousel from '$lib/components/EventCarousel.svelte';
	import eventsData from "./events.json";

	type EventsData = {
		events: Array<{
			folder: string,
			name: string,
			imageUrls: Array<string>,
		}>;
	}

	let events: EventsData = eventsData;
</script>

<body>
	<NavBar showCAlways={true} />

	<div class="content">
		<h1>Events</h1>

		{#each events.events as event}
			<h2>{event.name}</h2>
			<EventCarousel bind:imageLinks={event.imageUrls} />
		{/each}
	</div>
</body>

<style>
	.divider {
		height: 2rem;
	}

	h2 {
		margin: 0;
	}
</style>
