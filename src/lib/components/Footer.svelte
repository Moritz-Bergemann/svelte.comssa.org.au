<script>
	import Socials from "./Socials.svelte";

</script>

<div class="footer">
	<div class="footer-item">
        <div class="wrapper">
            <h1>Computer Science Students Association</h1>
            <p>
                Department of Computing <br />
                Building 314 <br /><br />
    
                Curtin University<br />
                Kent Street<br />
                Bentley WA 6102<br />
            </p>
        </div>
	</div>
	<div class="footer-item">
		<img src="/assets/comssa-logo-white.png" />
		<p class="center-text">&#169; ComSSA 2023</p>
        <p class="center-text"><a class="underlined" href="https://github.com/ComSSA">See the source code here!</a></p>
        <p class="center-text">Design by <a class="underlined" href="https://github.com/Moritz-Bergemann/">Moritz Bergemann</a></p>
	</div>
	<div class="footer-item" >
        <div class="wrapper">
            <h1 class="center-text">Get in touch!</h1>
			<br>
			
			<Socials color="#FFFFFF"/>

			<br>
			<a href="mailto://club@comssa.org.au">
				<h2 class="center-text">club@comssa.org.au</h2>
			</a>
        </div>
    </div>
</div>

<style>
	h1 {
		color: white;
		font-size: 1rem;
		text-align: left;
	}

	h2 {
		color: white;
		font-size: 1rem;
		text-align: left;
		font-weight: lighter;
	}

	a {
		text-decoration: none;
	}

	.underlined {
		text-decoration: underline;
	}

	p {
		color: white;
		font-size: 0.8rem;
	}

	a {
		color: white;
	}

	.footer {
		height: 12rem;
		background-color: var(--comssa-blue);
		margin-top: 5rem;
        padding-left: 5rem;
        padding-right: 5rem;
		padding-top: 1.5rem;
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		justify-content: space-evenly;
	}

	.footer-item {
		width: 30%;
		align-items: center;
	}

    .wrapper {
        margin: auto;
        display: block;
    }

    .center-text {
        text-align: center;
        margin-top: 0.3rem;
        margin-bottom: 0.3rem;
    }

	img {
		margin-top: 2rem;
		max-width: 5rem;
		display: block;
		margin: auto;
        margin-bottom: 2rem;
	}
</style>
