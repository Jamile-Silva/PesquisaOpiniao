<template>
  <div>
    <div id="supergraphic"></div>
    <header>
      <div class="header_logo">
          <img class="logo" src="@/static/logoBosch.svg"/>
      </div>
    </header>
    <main>
    
      <span>Meus Formularios (1)</span>
      <span class="p-input-icon-right">
          
          <InputText type="text" placeholder="Pesquise aqui..."/>
          <i class="pi pi-search" />
      </span>
      <div class="create_form">


        <div class="forms">
          <h3>Nome do Formulario</h3>
          <h5> 13 Perguntas</h5>
          <h5> 2 Respostas</h5>

          <Button icon="pi pi-pencil" class="p-button-text" /></footer>
          <Button icon="pi pi-trash" class="p-button-text" /></footer>
          <Button icon="pi pi-chart-bar" class="p-button-text" /></footer>
        </div>

        

      </div>

    </main>
    <footer>
      <Button icon="pi pi-plus" class="p-button-text" /></footer>
  </div>
</template>

<script>
export default {
  name: 'IndexPage'
}
</script>

<style lang="scss" scoped>

#supergraphic{
  background-image: url("@/static/supergraphic.svg");
  background-size: cover;
  height: 1vh;
  width: 100%;
}

header{
  .header_logo{
    height: 10vh;
    width: 100%;
    box-shadow: 0px 1px 5px var(--gray_shadow);
  }
  .logo{
    height: 100%;
  }
}

main{
  height: 79vh;

  .create_form{
    background: red;
    height: 500px;
    width: 850px;
    border-radius: 6px;
    box-sizing: border-box; //para criar uma borda interna
    padding: 30px; //tamanho da borda interna
    overflow-y:scroll;
  }
  .forms{
    background: var(--gray_light);
  }
}

footer{
  height: 10vh;
}

</style>
