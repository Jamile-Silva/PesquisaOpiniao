<template>
  <div>
    <div id="supergraphic"></div>
    <header>
      <div class="header_logo">
          <img class="logo" src="@/static/logoBosch.svg"/>
      </div>
    </header>
    <main>
    
      <div class="edit_form"></div>

    </main>
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
  background-color: var(--gray_light);
  height: 89vh;
  display: flex;
  align-items: center;
  justify-content: center;

  .edit_form{
    background: var(--white_absolute);
    height: 500px;
    width: 850px;
    border-radius: 6px;
    box-sizing: border-box; //para criar uma borda interna
    padding: 30px; //tamanho da borda interna
    overflow-y:scroll;
  }
}


</style>
