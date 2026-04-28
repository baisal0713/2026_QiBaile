using DG.Tweening;
using UnityEngine;

/// <summary>Darkens all materials on a renderer when the player stops moving.
/// Restores original colors when the player moves again.</summary>
public class BackroomsController : MonoBehaviour
{
    //==================== CONFIG =====================
    [Header("Player")]
    [Tooltip("The player's Transform — used to detect movement")]
    [SerializeField] private Transform player;

    [Header("Target")]
    [Tooltip("Renderer whose materials to darken")]
    [SerializeField] private Renderer targetRenderer;

    [Header("Timing")]
    [Tooltip("Seconds of no movement before darkening begins")]
    [Min(0f)]
    [SerializeField] private float idleGracePeriod = 2f;
    [Tooltip("How long the darken / brighten animation takes")]
    [Min(0.01f)]
    [SerializeField] private float animationDuration = 3f;
    [Tooltip("Tween easing for darken and brighten")]
    [SerializeField] private Ease ease = Ease.InOutSine;

    [Header("Detection")]
    [Tooltip("Minimum distance per frame to count as movement")]
    [Min(0f)]
    [SerializeField] private float moveThreshold = 0.01f;

    //==================== STATE =====================
    private Material[] _materials;
    private Color[] _originalColors;
    private Tween[] _tweens;

    private Vector3 _lastPosition;
    private float _idleTimer;
    private bool _isDark;

    //==================== LIFECYCLE =====================
    private void Start()
    {
        if (!targetRenderer || !player) return;

        // Cache instanced materials and their original colors
        _materials = targetRenderer.materials;
        _originalColors = new Color[_materials.Length];
        _tweens = new Tween[_materials.Length];

        for (int i = 0; i < _materials.Length; i++)
        {
            if (_materials[i].HasProperty("_Color"))
                _originalColors[i] = _materials[i].GetColor("_Color");
        }

        _lastPosition = player.position;
    }

    private void Update()
    {
        if (_materials == null || !player) return;

        bool isMoving = Vector3.Distance(player.position, _lastPosition) > moveThreshold;
        _lastPosition = player.position;

        if (isMoving)
        {
            _idleTimer = 0f;

            if (_isDark)
                Brighten();
        }
        else
        {
            _idleTimer += Time.deltaTime;

            if (!_isDark && _idleTimer >= idleGracePeriod)
                Darken();
        }
    }

    //==================== PRIVATE =====================
    private void Darken()
    {
        _isDark = true;
        AnimateAll(Color.black);
    }

    private void Brighten()
    {
        _isDark = false;

        for (int i = 0; i < _materials.Length; i++)
        {
            if (!_materials[i].HasProperty("_Color")) continue;

            KillTween(i);
            _tweens[i] = _materials[i]
                .DOColor(_originalColors[i], "_Color", animationDuration)
                .SetEase(ease);
        }
    }

    private void AnimateAll(Color color)
    {
        for (int i = 0; i < _materials.Length; i++)
        {
            if (!_materials[i].HasProperty("_Color")) continue;

            KillTween(i);
            _tweens[i] = _materials[i]
                .DOColor(color, "_Color", animationDuration)
                .SetEase(ease);
        }
    }

    private void KillTween(int index)
    {
        if (_tweens[index] is { active: true })
            _tweens[index].Kill();
    }

    private void OnDestroy()
    {
        if (_materials == null) return;

        for (int i = 0; i < _materials.Length; i++)
        {
            KillTween(i);
            if (_materials[i] && Application.isPlaying)
                Destroy(_materials[i]);
        }
    }
}
