<script lang="ts">
	import NavBar from '$lib/NavBar/NavBar.svelte';

	import EventCarousel from '$lib/EventCarousel.svelte';

	let bgnImageLinks1 = [
		'/assets/events/board-games-night-2023/2.JPG',
		'/assets/events/board-games-night-2023/3.JPG',
		'/assets/events/board-games-night-2023/4.JPG',
		'/assets/events/board-games-night-2023/6.JPG',
		'/assets/events/board-games-night-2023/7.JPG',
		'/assets/events/board-games-night-2023/8.JPG',
		'/assets/events/board-games-night-2023/9.JPG',
		'/assets/events/board-games-night-2023/10.JPG',
	];

	let bgnImageLinks2 = [
		'/assets/events/board-games-night-2023/11.JPG',
		'/assets/events/board-games-night-2023/12.JPG',
		'/assets/events/board-games-night-2023/13.JPG',
		'/assets/events/board-games-night-2023/14.JPG',
		'/assets/events/board-games-night-2023/15.JPG',
		'/assets/events/board-games-night-2023/16.JPG',
		'/assets/events/board-games-night-2023/17.JPG',
		'/assets/events/board-games-night-2023/18.JPG',
	];
</script>

<body>
	<NavBar showCAlways={true} />

	<div class="content">
		<h1>Events</h1>

		<h2>Board Games Night 2023</h2>
		<EventCarousel bind:imageLinks={bgnImageLinks1} />

		<h2>Board Games Night 2024</h2>
		<EventCarousel bind:imageLinks={bgnImageLinks2} />
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
