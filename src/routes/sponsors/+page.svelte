<script lang="ts">
	import NavBar from '$lib/NavBar/NavBar.svelte';

    let logosCdn = {
        atlassian:"https://res.cloudinary.com/dec6mijn3/image/upload/v1685100584/ComSSA-Website/Sponsors/atlassian-svg.svg",
        mechanicalRock:"https://res.cloudinary.com/dec6mijn3/image/upload/v1691423184/ComSSA-Website/Sponsors/mechanical-rock.webp",
        vgw:"https://res.cloudinary.com/dec6mijn3/image/upload/v1685099269/ComSSA-Website/Sponsors/vgw-new.png",
        rediSoftware:"https://res.cloudinary.com/dec6mijn3/image/upload/v1679834809/ComSSA-Website/Sponsors/redi-software.png",
        tomahawkLabs:"https://res.cloudinary.com/dec6mijn3/image/upload/v1679834808/ComSSA-Website/Sponsors/tomahawk-labs.png",
        imcTrading: "https://res.cloudinary.com/dec6mijn3/image/upload/v1679834808/ComSSA-Website/Sponsors/imc.png",
        eecms: "https://res.cloudinary.com/dec6mijn3/image/upload/v1686988749/ComSSA-Website/Sponsors/eecms.png",
    };

    let logosLocal = {
        atlassian: "/assets/sponsor-logos/atlassian",
        mechanicalRock: "/assets/sponsor-logos/mechanical-rock",
        vgw: "/assets/sponsor-logos/vgw",
        rediSoftware: "/assets/sponsor-logos/redi-software",
        tomahawkLabs: "/assets/sponsor-logos/tomahawk-labs",
        imcTrading: "/assets/sponsor-logos/imc-trading",
        eecms: "assets/sponsor-logos/eecms",
    };

    let logos = logosCdn;
</script>

<body>
	<NavBar showCAlways={true} />

    <div class="content">
        <div class="divider"/>
        <h1>Sponsors</h1>

        <div>
            <p> ComSSA is grateful to be working with the following organisations to provide opportunities and the best possible experience for our members. </p>
        </div>

        <div class="divider"/>

        <h3>
            Tier 3 (Gold) Sponsors THESE ARE MADE UP I DONT KNOW
        </h3>

        <div class="logos-section">
            <img src={logos.vgw} alt="VGW logo"/>
            <img src={logos.mechanicalRock} alt="Mechanical Rock logo"/>
            <img src={logos.rediSoftware} alt="Redi Software logo"/>
        </div>

        <h3>
            Tier 2 (Silver) Sponsors THESE ARE MADE UP I DONT KNOW
        </h3>

        <div class="logos-section">
            <img src={logos.tomahawkLabs} alt="Tomahawk Labs logo"/>
            <img src={logos.imcTrading} alt="IMC Trading logo"/>
            <img src={logos.atlassian} alt="Atlassian logo"/>
        </div>

        <div>
            <p>ComSSA is proudly partnered with the Curtin School of Electrical Engineering, Computing and Mathematical Sciences.</p>
        </div>

        <div class="partner-section">
            <img src={logos.eecms} alt="EECMS logo"/>
        </div>
	</div>
</body>

<style>
    .divider {
        height: 1rem;
    }

    .logos-section {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        flex-wrap: wrap;
    }

    .logos-section img {
        max-width: 20rem;
        max-height: 5rem;
        object-fit: contain;
        margin: 1rem;
    }

    .partner-section {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        flex-wrap: wrap;
    }

    .partner-section img {
        max-width: 15rem;
        max-height: 15rem;
        object-fit: contain;
        margin: 1rem;
    }

    h3 {
        margin-bottom: 0.5rem;
    }
</style>