public abstract class GameElement
{
    // Атрибути та властивості ...

    public virtual void Action(Engine engine)
    { }
    public virtual void ChangeSpeed(bool isBoosting)
    { }
    public abstract void Draw();
}

public abstract class Obstacle : GameElement
{
    public double Speed { get; set; }
    public Direction Direction { get; set; }
    public override bool isKilling { get { return false; } }

    // Інші атрибути та властивості...

    // Інші методи ...

}

public class Car : Obstacle
{
    protected const string car = "[###]";
    public override int Length { get { return car.Length; } }
    public override bool isKilling { get { return true; } }

    // Інші методи та властивості ...

    public override void ChangeSpeed(bool isBoosting)
    {
        var speedModifier = isBoosting ? 1 / 5.0 : 5.0;
        Speed *= speedModifier;
    }
}