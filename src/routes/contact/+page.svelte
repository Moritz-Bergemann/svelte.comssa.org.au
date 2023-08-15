<script lang="ts">
	import NavBar from '$lib/components/NavBar/NavBar.svelte';
	import Socials from '$lib/components/Socials.svelte';
</script>

<body>
	<NavBar showCAlways={true} />

	<div class="content">
		<h1>Contact Us</h1>

		<div>
			<p>TODO text that goes here - where should people contact ComSSA?</p>

			<p>
				For additional or business enquiries, please contact us at <b
					><a class="comssa-blue-text" href="mailto://club@comssa.org.au">club@comssa.org.au</a></b
				>.
			</p>
		</div>
        
        <div class="divider"/>
        <h2>Social Media</h2>
        <Socials color=""/>
	</div>
</body>

<style>
	.divider {
		height: 1rem;
	}
</style>
