<script lang="ts">
	import NavBar from '$lib/NavBar.svelte';
</script>

<body>
	<NavBar dynamic={false}/>

    <div class="content">
        <div class="divider"/>
        <h1>Events</h1>

        <div>
            <p>Events go here</p>
        </div>
	</div>
</body>

<style>
    .divider {
        height: 2rem;
    }
</style>