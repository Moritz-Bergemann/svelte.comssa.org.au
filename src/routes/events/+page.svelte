<script lang="ts">
	import NavBar from '$lib/NavBar/NavBar.svelte';

    import EventCarousel from '$lib/EventCarousel.svelte';
</script>

<body>
	<NavBar showCAlways={true} />

    <div class="content">
        <h1>Events</h1>
        
        <h2>Board Games Night 2023</h2>
        <EventCarousel/>

        <h2>Board Games Night 2024</h2>
        <EventCarousel/>
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