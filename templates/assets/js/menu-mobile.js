export default function mobile(){
    const d=document,
        $background=d.querySelector(".blackBackground"),
        $menuHead=d.querySelector(".user"),
        $menuBody=d.querySelector(".aside-nav");

    d.addEventListener("touchstart", (e)=>{
        if(e.target.matches(".hamburger-menu") || e.target.matches(".user") || e.target.matches(".aside-nav")){
            $menuHead.style.visibility="visible";
            $menuBody.style.visibility="visible";
            $menuHead.style.opacity=1;
            $menuBody.style.opacity=1;
            $background.style.opacity=1;
            $background.classList.add("visible");
        } else {
            $menuHead.style.visibility="hidden";
            $menuBody.style.visibility="hidden";
            $menuHead.style.opacity=0;
            $menuBody.style.opacity=0;
            $background.style.opacity=0;
            $background.classList.remove("visible");
        }
    });

}