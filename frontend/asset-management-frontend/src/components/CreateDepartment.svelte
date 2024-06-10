<script>
  import axios from 'axios';

  let name = '';

  const createDepartment = async () => {
    try {
      await axios.post('http://127.0.0.1:8000/departments/', { name });
      alert('Department created successfully');
      name = '';
    } catch (error) {
      console.error('Error creating department:', error);
    }
  };
</script>

<h2>Create Department</h2>
<form on:submit|preventDefault={createDepartment}>
  <input bind:value={name} type="text" placeholder="Department Name" />
  <button type="submit">Create</button>
</form>
