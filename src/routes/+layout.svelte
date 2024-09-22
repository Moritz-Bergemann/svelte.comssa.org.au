<script>
	import Footer from '$lib/components/Footer.svelte';
import '../styles/app.css';
</script>


<svelte:head>
	<title>ComSSA</title>
	<meta name="description" content="Computer Science Student's Association at Curtin University"/>
	<meta name="keywords" content="Computing, Students, Club, Association, Curtin University"/>
	<style>
		@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600:ital@0;1&display=swap');
	</style>
</svelte:head>

<slot />

<Footer/>