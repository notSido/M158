<script>
  import { onMount } from 'svelte';
  import axios from 'axios';

  let assets = [];

  onMount(async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/assets/');
      assets = response.data;
    } catch (error) {
      console.error('Error fetching assets:', error);
    }
  });
</script>

<h2>Assets</h2>
<ul>
  {#each assets as asset}
    <li>{asset.name} ({asset.type}) - {asset.serial_nr}</li>
  {/each}
</ul>
