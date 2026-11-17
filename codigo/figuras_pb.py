import sys, pandas as pd, matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt, matplotlib.dates as mdates
R=sys.argv[1]; OUT=sys.argv[2]
base=pd.read_csv(f"{R}/dados/processados/base_diaria.csv",parse_dates=["data"],index_col="data").iloc[1:]
mov=pd.read_csv(f"{R}/resultados/correlacoes_moveis.csv",parse_dates=["data"],index_col="data")
anos=pd.read_csv(f"{R}/resultados/correlacao_por_ano.csv")
E={"font.size":12,"axes.labelsize":12,"xtick.labelsize":11,"ytick.labelsize":11,"legend.fontsize":11,
   "axes.spines.top":False,"axes.spines.right":False,"font.family":"DejaVu Sans","axes.edgecolor":"black"}
with plt.rc_context(E):
    fig,ax=plt.subplots(figsize=(11,5.2))
    ind=base["crise_global"].astype(int); g=(ind!=ind.shift()).cumsum(); first=True
    for _,s in ind[ind==1].groupby(g[ind==1]):
        ax.axvspan(s.index[0],s.index[-1],color="#d0d0d0",lw=0,zorder=0,label="Crise global (VIX > 30)" if first else None); first=False
    ax.plot(mov.index,mov["corr63_eua"],color="black",lw=1.4,label="EUA: S&P 500 x Treasury 10 anos")
    ax.plot(mov.index,mov["corr63_br"],color="#707070",lw=1.4,ls=(0,(4,1.5)),label="Brasil: Ibovespa x NTN-B (IMA-B)")
    ax.axhline(0,color="black",lw=0.8); ax.set_ylim(-0.85,0.95); ax.set_ylabel("Correlação móvel (63 pregões)")
    ax.xaxis.set_major_locator(mdates.YearLocator(2)); ax.xaxis.set_major_formatter(mdates.DateFormatter("%Y"))
    ax.legend(loc="upper left",ncol=3,frameon=False,bbox_to_anchor=(0,1.1)); fig.tight_layout()
    fig.savefig(f"{OUT}/figura1_pb.png",dpi=300); plt.close(fig)
    fig,ax=plt.subplots(figsize=(11,4.8))
    ax.axvspan(2021.5,2022.5,color="#d0d0d0",lw=0,zorder=0); ax.text(2022,0.86,"2022",ha="center",fontsize=11)
    ax.plot(anos["ano"],anos["corr_eua"],color="black",lw=1.6,marker="o",ms=6,mfc="black")
    ax.plot(anos["ano"],anos["corr_br"],color="#606060",lw=1.6,ls="--",marker="s",ms=6,mfc="white",mec="#303030")
    ax.text(2026.35,anos["corr_br"].iloc[-1]+0.06,"Brasil",fontsize=12,fontweight="bold",va="center")
    ax.text(2026.35,anos["corr_eua"].iloc[-1]-0.06,"EUA",fontsize=12,fontweight="bold",va="center")
    ax.axhline(0,color="black",lw=0.8); ax.set_xlim(2003.5,2027.3); ax.set_ylim(-0.75,0.95); ax.set_xticks(range(2004,2027,2))
    ax.set_ylabel("Correlação dos retornos diários no ano"); fig.tight_layout()
    fig.savefig(f"{OUT}/figura2_pb.png",dpi=300); plt.close(fig)
