import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    TA: 20,
    TR: 22,
    RH: 50,
    VEL: 0.1,
    CLO: 1,
    MET: 1.3,
    POINTPPD: [],
    PLOTCONFORT: [],
  },
  mutations: {
    setTair(state, TA) {
      state.TA = TA;
    },
    setTray(state, TR) {
      state.TR = TR;
    },
    setHrel(state, RH) {
      state.RH= RH;
    },
    setVair(state, VEL) {
      state.VEL = VEL;
    },
    setClo(state, CLO) {
      state.CLO = CLO;
    },
    setMet(state, MET) {
      state.MET = MET;
    },
    setPointPpd(state, POINTPPD) {
      state.POINTPPD = POINTPPD;
    },
    setPlotConfort(state, PLOTCONFORT) {
      state.PLOTCONFORT = PLOTCONFORT;
    }
  },
  actions: {},
  modules: {},
  getters: {
    getPMV(state){
      return state.PMV;
    },
    getPPD(state){
      return state.PPD;
    },
    getTair(state){
      return state.TA;
    },
    getTray(state){
      return state.TR;
    },
    getHrel(state){
      return state.RH;
    },
    getVair(state){
      return state.VEL;
    },
    getClo(state){
      return state.CLO;
    },
    getMet(state){
      return state.MET;
    },
    getPoitPpd(state) {
      return state.POINTPPD;
    },
    getPlotConfort(state) {
      return state.PLOTCONFORT;
    }
  }
})