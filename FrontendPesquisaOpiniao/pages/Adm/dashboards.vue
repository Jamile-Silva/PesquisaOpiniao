<template>
  <div>
    <div id="supergraphic"></div>
    <header>
      <div class="header_logo">
          <img class="logo" src="@/static/logoBosch.svg"/>
      </div>
    </header>

      <!-- <h3>Resultados - Pesquisa de Opinião</h3> -->
    
    <main>    
      <!-- <div v-for="index in formularios" :key="index">
        {{index.fkPesquisa}}
        <div v-for="item in formularios" :key="item">
          Pergunta {{item.enunciado}}
          <Chart type="pie" :data="chartData" :options="lightOptions" />
        </div>
      </div> -->
    <button v-on:click="teste()"></button>
    </main>

    <footer></footer>

  </div>
</template>

<script>
export default {
  name: 'IndexPage',
  created(){
    this.$axios.get(this.$store.state.BASE_URL + "resposta").then((response)=>{
        this.respostas = response.data;
        console.log('Respostas',response.data)
      })

      this.$axios.get(this.$store.state.BASE_URL + "formulario").then((response)=>{
        this.formularios = response.data;
        console.log('Formularios',response.data)
      })

      this.$axios.get(this.$store.state.BASE_URL + "pesquisa").then((response)=>{
        this.pesquisas = response.data;
        console.log('Pesquisas', response.data)
     })
  },
  data() {
    return {
      chartData: {
        labels: ['Resposta 1','Reposta 2','Resposta 3'],
        datasets: [{
          data: [5, 15, 4],
          backgroundColor: ["#42A5F5","#66BB6A","#FFA726"],
          hoverBackgroundColor: ["#64B5F6","#81C784","#FFB74D"]
          }]
        },
        lightOptions: {
          plugins: {
            legend: {
              labels: {
                color: 'black'
              }
            }
          }
        },
      pesquisas: "",
      formularios: "",
      respostas: "",
      i:"",
      a:"",
    }
  },
  methods:{
    teste:function(){
      for(this.i in this.formularios){
        console.log('Esse é o enunciado', this.formularios[this.i].enunciado)
        for(this.a in this.formularios.fkPesquisa){
          console.log('Essa é a pesquisa', this.formularios.fkPesquisa.nomePesquisa[this.a])
        }
      }
    }
  }
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
  height: 89vh;
  display: flex;
  align-items: center;
  justify-content: center;

}


</style>
