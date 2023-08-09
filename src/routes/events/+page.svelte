<script lang="ts">
	import NavBar from '$lib/NavBar.svelte';

    import EventCarousel from '$lib/EventCarousel.svelte';
</script>

<body>
	<NavBar dynamic={false}/>

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