<script>
  import { onMount } from 'svelte';
  import axios from 'axios';

  let departments = [];

  onMount(async () => {
    try {
      const response = await axios.get('http://127.0.0.1:8000/departments/');
      departments = response.data;
    } catch (error) {
      console.error('Error fetching departments:', error);
    }
  });
</script>

<h2>Departments</h2>
<ul>
  {#each departments as department}
    <li>{department.name}</li>
  {/each}
</ul>
