<script>
	import Footer from '$lib/components/Footer.svelte';
	import '../styles/app.css';
	import { theme } from '$lib/theme';
	import { browser } from '$app/environment';

	if (browser) {
		const currentTheme = localStorage.getItem('theme');

		if (currentTheme === 'dark') {
			theme.set('dark');
		}
	}

	theme.subscribe((value) => {
		if (browser) {
			if (value === 'dark') {
				document.body.classList.add('dark-theme');
			} else if (value === 'light') {
				document.body.classList.remove('dark-theme');
			}

			localStorage.setItem('theme', value);
		}
	});
</script>

<svelte:head>
	<title>ComSSA</title>
	<meta name="description" content="Computer Science Student's Association at Curtin University" />
	<meta name="keywords" content="Computing, Students, Club, Association, Curtin University" />
	<style>
		@import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600:ital@0;1&display=swap');
	</style>
</svelte:head>

<slot />

<Footer />
